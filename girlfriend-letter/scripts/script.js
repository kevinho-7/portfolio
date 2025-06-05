const elements = document.querySelectorAll('.fade-up-on-scroll');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
});

elements.forEach(el => observer.observe(el));
