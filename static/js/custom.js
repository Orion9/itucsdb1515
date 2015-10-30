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
$(function() {
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
                    $('#op-main-success-alert').show();
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

    $('#update-rows-button').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-update-person').modal('show');
            var user_data = selected_row[0];
            $('#modal-update-person-id').val(user_data[0]);
            $('#modal-update-person-name').val(user_data[1]);

            //Let us arrange date value a little bit.
            var date_array = user_data[2].split('/');
            var date = date_array[2] + "-" + date_array[1] + "-" + date_array[0];

            $('#modal-update-person-bday').val(date);
            $('#modal-update-person-bplace').val(user_data[3]);
            $('#modal-update-person-type').val(user_data[4]);

            console.log(user_data);
        }
    });

    $('#modal-update-form').submit(function(){
        var data = {
            person_id: $('#modal-update-person-id').val(),
            person_name: $('#modal-update-person-name').val(),
            person_birth_date: $('#modal-update-person-bday').val(),
            person_birth_place: $('#modal-update-person-bplace').val(),
            person_type: $('#modal-update-person-type').val()
        };

       $.ajax({
           url: "/api/person/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-person').modal('hide');
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
    });
} );

// Hides alert. Prevents them to be destroyed from DOM.
$(function(){
    $('#op-error-close').click( function(){
            $('#op-error-alert').hide();
            $('#op-main-error-alert').hide();
            $('#log-main-error-alert').hide();
        }
    )
});

$(function(){
   $('#op-update-close').click(function(){
            $('#op-update-error-alert').hide();
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
                    $('#op-main-success-alert').show();
                    location.reload();
                } else {
                    $('#op-main-error-alert').show();
                    $('#add-new-person').modal('hide');
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

// Add Type POST Handler
// Handles add type modal's POST data
$(document).ready(function() {
    $('#modal-add-type-form').submit(function() {
        var user_data = {
                person_type: $('#add-modal-person-type').val()
            };

        $.ajax({
            url: "/api/person/type/add",
            contentType: 'application/json',
            data: JSON.stringify(user_data),
            type: "POST",
            dataType : "json",
            success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#add-new-person-type').hide();
                    location.reload();
                } else {
                    $('#op-main-error-alert').show();
                    $('#add-new-person-type').hide();
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
