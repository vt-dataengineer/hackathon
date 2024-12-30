document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll("h1, p");
    elements.forEach((el) => {
        el.style.opacity = 0;
        el.style.transition = "opacity 1s";
        setTimeout(() => {
            el.style.opacity = 1;
        }, 200);
    });
});
