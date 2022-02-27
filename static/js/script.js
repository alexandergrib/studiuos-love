/*           Top Arrow              */
$('#arrow').hide();
var altura = $('header').outerHeight();
var des = $(window).scrollTop();
$(window).on('scroll', function () {

    des = $(window).scrollTop();

    if (des > altura) {
        $('#arrow').fadeIn();
    } else {
        $('#arrow').fadeOut();
    }

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