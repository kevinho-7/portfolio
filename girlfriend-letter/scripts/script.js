const elements = document.querySelectorAll('.fade-up-on-scroll');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
});

elements.forEach(el => observer.observe(el));

document.addEventListener("DOMContentLoaded", () => {
  const clickSong = document.getElementById("btn1");
  const song = document.getElementById("song");
  const slide1 = document.getElementById("slide1");

  clickSong.addEventListener("click", () => {
    song.play();
    slide1.scrollIntoView();
  });

  window.onload = function () {
    const loader = document.querySelector(".loader");

    setTimeout(() => {
      loader.classList.add("hide");

      setTimeout(() => {
        loader.style.display = "none";
      }, 800); 
    }, 5000); 
  };
  
});