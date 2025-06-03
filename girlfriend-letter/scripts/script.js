const playPauseBtn = document.getElementById('playPauseBtn');
const progressBar = document.querySelector('.progress-bar');
const currentTimeSpan = document.getElementById('currentTime');
const durationSpan = document.getElementById('duration');

let audio = new Audio('https://file-examples.com/storage/fe9f6f893066954d9aac3a2/2017/11/file_example_MP3_700KB.mp3');
let isPlaying = false;

function togglePlayPause() {
    if (isPlaying) {
        audio.pause();
        playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
    } else {
        audio.play();
        playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
    }
    isPlaying = !isPlaying;
}

function updateProgress() {
    const progress = (audio.currentTime / audio.duration) * 100;
    progressBar.style.width = `${progress}%`;
    progressBar.setAttribute('aria-valuenow', progress);
    
    currentTimeSpan.textContent = formatTime(audio.currentTime);
    durationSpan.textContent = formatTime(audio.duration);
}

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

playPauseBtn.addEventListener('click', togglePlayPause);
audio.addEventListener('timeupdate', updateProgress);

new Vue({
  el: "#app",
  data() {
    return {
      isOpenedTop: true,
      items: [
        {
          img1: "images/santanna_wallpaper_2018.jpg",
          img2: "images/cat couple2.jpg",
          img3: "images/cat couple3.jpg",
          title: "COUPLE",
          isOpen: false,
        },
        {
          img1: "images/cat cute.jpg",
          img2: "images/cat cute 2.jpg",
          img3: "images/cat cute 3.jpg",
          title: "CUTE",
          isOpen: false,
        },
        {
          img1: "images/cat baby2.jpg",
          img2: "images/cat baby.jpg",
          img3: "images/cat baby3.jpg",
          title: "BABIES",
          isOpen: false,
        },
        {
          img1: "images/cat sleep.jpg",
          img2: "images/cat sleep2.jpg",
          img3: "images/cat sleep 3.jpg",
          title: "SLEEP",
          isOpen: false,
        },
        {
          img1: "images/CAT HERO1.jpg",
          img2: "images/cat hero2.jpg",
          img3: "images/cat hero3.jpg",
          title: "HERO",
          isOpen: false,
        },
      ],
    };
  },
  methods: {
    topOpen() {
      this.isOpenedTop = !this.isOpenedTop;
    },

    open(idx, isOpen) {
      if (this.isOpenedTop) {
        this.items[idx].isOpen = !isOpen;
      }
    },

    reset() {
      this.items.forEach((item) => (item.isOpen = false));
      this.isOpenedTop = false;
    },
  },
});
