// hero main3
const imagesContainer = document.querySelector(".images-container");
const btnPre = document.querySelector(".btn-pre");
const btnNext = document.querySelector(".btn-next");

const totalImages = document.querySelectorAll(".images-container img").length;
const imagesPerView = 3;

let currentIndex = 0;

function updateView() {
  const offset = -(currentIndex * (100 / imagesPerView));
  imagesContainer.style.transform = `translateX(${offset}%)`;
}

btnPre.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
    updateView();
  }
});

btnNext.addEventListener("click", () => {
  if (currentIndex < totalImages - imagesPerView) {
    currentIndex++;
    updateView();
  }
});

updateView();
// hero main5
const imgContainerProducts5 = document.querySelector(
  ".hero-main5-products-container"
);
const btn5Pre = document.querySelector(".hero-main5-pre");
const btn5Next = document.querySelector(".hero-main5-next");

const totalImages5 = document.querySelectorAll(".hero-main5-product").length;
const imagesPerView5 = 3;

let currentIndex5 = 0;

function updateView5() {
  const offset5 = -(currentIndex5 * (100 / imagesPerView5));
  imgContainerProducts5.style.transform = `translateX(${offset5}%)`;
}

btn5Pre.addEventListener("click", () => {
  if (currentIndex5 > 0) {
    currentIndex5--;
    updateView5();
  }
});

btn5Next.addEventListener("click", () => {
  if (currentIndex5 < totalImages5 - imagesPerView5) {
    currentIndex5++;
    updateView5();
  }
});

updateView5();
