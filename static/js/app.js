(function () {
  const STORAGE_KEY = "theme";
  const DEFAULT_THEME = "light"; // light | dark

  const themeToggle = document.getElementById("themeToggle");

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);

    // Texto del botón
    if (themeToggle) {
      themeToggle.textContent = theme === "dark" ? "Modo claro" : "Modo oscuro";
    }
  }

  function getSavedTheme() {
    return localStorage.getItem(STORAGE_KEY) || DEFAULT_THEME;
  }

  function saveTheme(theme) {
    localStorage.setItem(STORAGE_KEY, theme);
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute("data-bs-theme") || DEFAULT_THEME;
    const next = current === "dark" ? "light" : "dark";
    applyTheme(next);
    saveTheme(next);
  }

  // Init
  const initialTheme = getSavedTheme();
  applyTheme(initialTheme);

  if (themeToggle) {
    themeToggle.addEventListener("click", toggleTheme);
  }
})();
