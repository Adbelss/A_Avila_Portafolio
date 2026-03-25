document.addEventListener("DOMContentLoaded", function () {
  const animatedItems = document.querySelectorAll("[data-reveal]");

  if ("IntersectionObserver" in window && animatedItems.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15
    });

    animatedItems.forEach((item) => {
      observer.observe(item);
    });
  }
});
