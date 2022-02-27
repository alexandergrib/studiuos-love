/*           Top Arrow              */

var height = $('header').outerHeight();

document.addEventListener("DOMContentLoaded", () => {
  
    const goTopButton = document.querySelector(".go-to-top");

    window.addEventListener("scroll", () => {
        if (window.scrollY > height) {
            goTopButton.style.display = "flex";
        } else {
            goTopButton.style.display = "none";
        }
    });

});