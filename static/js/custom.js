/**
 * Created by Oguz Kerem Tural on 10/23/2015.
 * Makes it possible to use optional libraries from bootstrap.js
 * Also extends js library with new functions
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

$(document).ready(function() {
    $('#modal-submit-form').submit(function() {
        var user_data = {user_email: $('#modal-login-email').val(), user_password: $('#modal-login-password').val()};
        $.ajax({
            url: "/api/login",
            contentType: 'application/json',
            data: JSON.stringify(user_data),
            type: "POST",
            dataType : "json",
            success: function( json, post_data ) {
                if ( json.result ) {
                    location.reload();
                } else {
                    $('#login-error-alert').show();
                }
                console.log(json);
            },
            error: function( xhr, status, errorThrown ) {
                console.log( "Sorry, there was a problem!" );
            }
        });
        json = '';
        return false;
    });
});