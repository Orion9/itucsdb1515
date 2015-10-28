/**
 * Created by Oguz Kerem Tural on 10/23/2015.
 * Makes it possible to use optional libraries from bootstrap.js
 * Also extends js library with new functions
 */

// User Login Handler
// Handles POST request coming from Auth API.
$(document).ready(function() {
    $('#modal-submit-form').submit(function() {
        var user_data = {user_email: $('#modal-login-email').val(), user_password: $('#modal-login-password').val()};
        $.ajax({
            url: "/api/login",
            contentType: 'application/json',
            data: JSON.stringify(user_data),
            type: "POST",
            dataType : "json",
            success: function( json ) {
                if ( json.result ) {
                    location.reload();
                } else {
                    $('#login-error-alert').show();
                }
                console.log( json );
            },
            error: function( ) {
                console.log( "TROUBLE!" );
            }
        });
        return false;
    });
});

// For enabling jQuery Data Tables
$(document).ready(function() {
    var glorious_table = $('#glorious-table').DataTable();

    $('#glorious-table-body').on('click', 'tr', function() {
        if ( $( this ).hasClass('selected') )
        {
            $( this ).removeClass('selected');
        }
        else
        {
            $( this ).addClass('selected')
        }
    });

    $('#delete-rows-button').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/person/delete",
            contentType: 'application/json',
            data: JSON.stringify(data),
            type: "POST",
            dataType : "json",
            success: function( json ) {
                if ( json.result ) {
                    location.reload();
                } else {
                    $('#op-main-error-alert').show();
                }
                console.log( json );
            },
            error: function( ) {
                console.log( "TROUBLE!" );
            }
        });
        console.log(data);
    });
} );

// Hides alert. Prevents them to be destroyed from DOM.
$(function(){
    $('#op-error-close').click( function(){
            $('#op-error-alert').hide();
            $('#op-main-error-alert').hide();
        }
    )
});

$(function(){
    $('#op-success-close').click( function(){
            $('#op-main-success-alert').hide();
        }
    )
});

// Add POST Handler
// Handles add modal's POST data
$(document).ready(function() {
    $('#modal-add-form').submit(function() {
        var user_data =
            {
                person_name: $('#modal-person-name').val(),
                person_birth_date: $('#modal-person-bday').val(),
                person_birth_place: $('#modal-person-bplace').val(),
                person_type: $('#modal-person-type').val()
            };

        $.ajax({
            url: "/api/person/add",
            contentType: 'application/json',
            data: JSON.stringify(user_data),
            type: "POST",
            dataType : "json",
            success: function( json ) {
                if ( json.result ) {
                    location.reload();
                } else {
                    $('#op-main-error-alert').show();
                    $('#modal-add-form').hide();
                }
                console.log( json );
            },
            error: function( ) {
                $('#op-main-error-alert').show();
                console.log( "TROUBLE!" );
            }
        });
        return false;
    });
});

