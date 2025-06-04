let currentPage = 0;
const pages = document.querySelectorAll('.page');

window.addEventListener('wheel', (e) => {
  if (e.deltaY > 0) {
    if (currentPage < pages.length - 1) currentPage++;
  } else {
    if (currentPage > 0) currentPage--;
  }

  pages[currentPage].scrollIntoView({ behavior: 'smooth' });
});
