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


// bootstrap popovers
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})


$('.add-poem').click(function(){
    $('.submit_poem').toggleClass('hide');
    if ($(".submit_poem").hasClass("hide")) {
        $('.add-poem').text($('.add-poem').text().replace("Hide form", 'Add new poem'));
    }else {
        $('.add-poem').text($('.add-poem').text().replace('Add new poem',"Hide form"));
    }
});