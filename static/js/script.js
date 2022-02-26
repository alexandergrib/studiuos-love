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