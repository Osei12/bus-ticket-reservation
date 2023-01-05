const Menu = document.querySelector(".menu");
const Close = document.querySelector(".close");
const Nav = document.querySelector("nav");

Menu.addEventListener("click", () => {
    Nav.classList.add("open-nav");
})

Close.addEventListener("click", () => {
    Nav.classList.remove("open-nav");
})