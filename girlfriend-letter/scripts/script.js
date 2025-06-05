
AOS.init({
  once: false,
  duration: 1000,
});

let currentPage = 0;
const pages = document.querySelectorAll(".page");

window.addEventListener("wheel", (e) => {
  if (e.deltaY > 0 && currentPage < pages.length - 1) {
    currentPage++;
  } else if (e.deltaY < 0 && currentPage > 0) {
    currentPage--;
  }
  pages[currentPage].scrollIntoView({ behavior: "smooth" });
});

let touchStartY = 0;

window.addEventListener("touchstart", (e) => {
  touchStartY = e.touches[0].clientY;
});

window.addEventListener("touchend", (e) => {
  const touchEndY = e.changedTouches[0].clientY;
  const deltaY = touchStartY - touchEndY;

  if (deltaY > 50 && currentPage < pages.length - 1) {
    currentPage++;
  } else if (deltaY < -50 && currentPage > 0) {
    currentPage--;
  }
  pages[currentPage].scrollIntoView({ behavior: "smooth" });
});