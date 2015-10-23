/**
 * Created by Oguz Kerem Tural on 10/23/2015.
 * Makes it possible to use optional libraries from bootstrap.js
 */

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

$(function () {
    $('[data-toggle="popover"]').popover();

    $("#userMenuPopover").popover({
        html: true,
        content: function(){
            return $('#userMenuPopoverContent').html();
        },
        placement: "bottom"
    });
});

$(function(){
    $('body').tooltip( {selector: '[data-toggle=tooltip]'} );
});