/**
 * Created by Oguz Kerem Tural on 10/23/2015.
 * Makes it possible to use optional libraries from bootstrap.js
 * Also extends js library with new functions
 */

// User Login Handler
// Handles POST request coming from Auth API.
$(document).ready(function() {
    // Login Form Handler
    $('#modal-submit-form').submit(function() {
        var user_data = {
            user_email: $('#modal-login-email').val(),
            user_password: $('#modal-login-password').val()
        };

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

    $('#map-button').click(function(){
        var element = $('#map-modal');

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0) {
            $('#op-update-error-alert').show();
        } else {
            element.modal('show');
            var user_data = selected_row[0];

            var coordinates = user_data[3];
            element.on('shown.bs.modal', function (){
                var iframes = $('iframe');
                for (var i = 0; i < iframes.length; i++) {
                    iframes[i].parentNode.removeChild(iframes[i]);
                }

                var innerHtml = '<iframe width="560" height="450" frameborder="0" style="border:0" ' +
                    'src="https://www.google.com/maps/embed/v1/place?key=AIzaSyCZGB4LyytNSiSk3hsmIrgM0ikaOO3NMUs&q=' +
                    coordinates + '&zoom=8" allowfullscreen> </iframe>';
                var map_element = document.getElementById("map-canvas");
                map_element.insertAdjacentHTML('beforeend', innerHtml)
            });

            console.log(user_data[3]);
        }
    });

    // Delete Person
    $('#delete-rows-button').click(function(event){
        event.preventDefault();
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

    // Delete City
    $('#delete-cities-button').click(function(event){
        event.preventDefault();
        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/city/delete",
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
    
    // Delete Country
    $('#delete-country').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/country/delete",
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

    // Delete Matches
    $('#delete-match').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/match/delete",
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

    // Delete League
    $('#delete-league').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/league/delete",
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

    // Delete Player
    $('#delete-player').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/player/delete",
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

    // Delete Team
    $('#delete-rows-button-team').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/team/delete",
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

    // Delete Sponsorship
    $('#delete-rows-button-sponsorship').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/sponsorship/delete",
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

    // Delete Stadium
    $('#delete-rows-button-stadium').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/stadium/delete",
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

    // Delete Penalties
    $('#penalty-delete-rows-button').click(function(){

        var data = [];
        var selected_rows = glorious_table.rows('.selected').data();
        for (var i = 0; i < selected_rows.length; ++i) {
            data[i] = (selected_rows[i][0]);
        }
        $.ajax({
            url: "/api/penalty/delete",
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

    // Update Person Button
    $('#update-rows-button').click(function(event){
        event.preventDefault();
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

    // Penalty Update Button
    $('#penalty-update-rows-button').click(function(event){
        event.preventDefault();
        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-update-penalty').modal('show');
            var user_data = selected_row[0];
            $('#modal-update-penalty-id').val(user_data[0]);
            $('#modal-update-penalty-name').val(user_data[1]);

            //Let us arrange date value a little bit.
            var date_array = user_data[2].split('/');
            var date = date_array[2] + "-" + date_array[1] + "-" + date_array[0];

            $('#modal-update-penalty-given-date').val(date);
            $('#modal-update-penalty-type').val(user_data[3]);

            console.log(user_data);
        }
    });

    // Update Person
    $('#modal-update-form').submit(function(event){
        event.preventDefault();
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
           error: function() {
                console.log( "TROUBLE!" );
           }
       });
    });

    // Update Penalty
    $('#modal-update-penalty').submit(function(event){
        event.preventDefault();
        var data = {
            penalty_id: $('#modal-update-penalty-id').val(),
            person_name: $('#modal-update-penalty-name').val(),
            penalty_given_date: $('#modal-update-penalty-given-date').val(),
            penalty_type: $('#modal-update-penalty-type').val()
        };

       $.ajax({
           url: "/api/penalty/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-penalty').modal('hide');

                    location.reload();
                } else {
                    $('#op-main-error-alert').show();
                }
                console.log( json );
            },
           error: function() {
                console.log( "TROUBLE!" );
           }
       });
    });

    // Update Team Button
    $('#update-teams-button').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-team-update').modal('show');

            var user_data = selected_row[0];
            $('#modal-update-team-id').val(user_data[0]);
            $('#modal-update-team-name').val(user_data[1]);
            $('#modal-update-team-couch').val(user_data[2]);

            console.log(user_data);
        }
    });

     // Update Team
    $('#modal-team-update-form').submit(function(event){
        event.preventDefault();
        var data = {
            team_id: $('#modal-update-team-id').val(),
            team_name: $('#modal-update-team-name').val(),
            team_couch: $('#modal-update-team-couch').val()
        };

       $.ajax({
           url: "/api/team/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-team').modal('hide');
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

    // Update City Button
    $('#update-cities-button').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-city-update').modal('show');

            var user_data = selected_row[0];
            $('#modal-update-city-id').val(user_data[0]);
            $('#modal-update-city-name').val(user_data[1]);
            $('#modal-update-city-population').val(user_data[2]);

            console.log(user_data);
        }
    });

     // Update City
    $('#modal-city-update-form').submit(function(event){
        event.preventDefault();
        var data = {
            city_id: $('#modal-update-city-id').val(),
            city_name: $('#modal-update-city-name').val(),
            city_population: $('#modal-update-city-population').val()
        };

       $.ajax({
           url: "/api/city/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-city').modal('hide');
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

    // Update Country Button
    $('#update-country').click(function(event){
        event.preventDefault();
        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-country-update').modal('show');
            var user_data = selected_row[0];
            $('#modal-update-country-id').val(user_data[0]);
            $('#modal-update-country-name').val(user_data[1]);
            $('#modal-update-country-population').val(user_data[2]);

            console.log(user_data);
        }
    });

    // Update Country
    $('#modal-country-update-form').submit(function(event){
        event.preventDefault();
        var data = {
            country_id: $('#modal-update-country-id').val(),
            country_name: $('#modal-update-country-name').val(),
            country_population: $('#modal-update-country-population').val()
        };

       $.ajax({
           url: "/api/country/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-country').modal('hide');
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

    // Update League Button
    $('#update-league').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-league-update').modal('show');
            var user_data = selected_row[0];
            $('#modal-update-league-id').val(user_data[0]);
            $('#modal-update-league-name').val(user_data[1]);
            $('#modal-update-league-country').val(user_data[2]);
            $('#modal-update-league-start-date').val(user_data[2]);

            console.log(user_data);
        }
    });

    // Update Player Button
    $('#update-player').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-player-update').modal('show');
            var user_data = selected_row[0];
            $('#modal-update-player-id').val(user_data[0]);
            $('#modal-update-player-name').val(user_data[1]);
            $('#modal-update-player-team').val(user_data[2]);
            $('#modal-update-player-goals').val(user_data[2]);

            console.log(user_data);
        }
    });

    // Update Player
    $('#modal-player-update-form').submit(function(){
        var data = {
            player_id: $('#modal-update-player-id').val(),
            player_name: $('#modal-update-player-name').val(),
            player_team: $('#modal-update-player-team').val(),
            player_goals: $('#modal-update-player-goals').val()
        };

       $.ajax({
           url: "/api/player/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-player').modal('hide');
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

    // Update League
    $('#modal-league-update-form').submit(function(){
        var data = {
            league_id: $('#modal-update-league-id').val(),
            league_name: $('#modal-update-league-name').val(),
            league_country: $('#modal-update-league-country').val(),
            league_start_date: $('#modal-update-league-start-date').val()
        };

       $.ajax({
           url: "/api/league/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-league').modal('hide');
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

    // Update Sponsorship Button
    $('#update-rows-button-sponsorship').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-sponsorship-update').modal('show');

            var user_data = selected_row[0];
            $('#modal-update-sponsorship-id').val(user_data[0]);
            $('#modal-update-sponsorship-name').val(user_data[1]);

            var date_array = user_data[2].split('/');
            var date = date_array[2] + "-" + date_array[1] + "-" + date_array[0];

            $('#modal-update-sponsorship-start-date').val(date);
            $('#modal-update-sponsorship-league').val(user_data[3]);
            $('#modal-update-sponsorship-team').val(user_data[4]);
            $('#modal-update-sponsorship-person').val(user_data[5]);

            console.log(user_data);
        }
    });

     // Update Sponsorship
    $('#modal-update-form-sponsorship').submit(function(event){
        event.preventDefault();
        var data = {
            sponsorship_id: $('#modal-update-sponsorship-id').val(),
            sponsorship_name: $('#modal-update-sponsorship-name').val(),
            sponsorship_start_date: $('#modal-update-sponsorship-start-date').val(),
            sponsorship_league: $('#modal-update-sponsorship-league').val(),
            sponsorship_team: $('#modal-update-sponsorship-team').val(),
            sponsorship_person: $('#modal-update-sponsorship-person').val()
        };

       $.ajax({
           url: "/api/sponsorship/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-sponsorship').modal('hide');
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

       // Update Stadium Button
    $('#update-rows-button-stadium').click(function(){

        var selected_row = glorious_table.rows('.selected').data();
        if (selected_row.length > 1 || selected_row.length === 0)
        {
            $('#op-update-error-alert').show();
        }
        else
        {
            $('#modal-stadium-update').modal('show');

            var user_data = selected_row[0];
            $('#modal-update-stadium-id').val(user_data[0]);
            $('#modal-update-stadium-name').val(user_data[1]);
            $('#modal-update-stadium-team').val(user_data[2]);
            $('#modal-update-stadium-location').val(user_data[3]);
            $('#modal-update-stadium-capacity').val(user_data[4]);

            console.log(user_data);
        }
    });

     // Update Stadium
    $('#modal-update-form-stadium').submit(function(event){
        event.preventDefault();
        var data = {
            stadium_id: $('#modal-update-stadium-id').val(),
            stadium_name: $('#modal-update-stadium-name').val(),
            stadium_team: $('#modal-update-stadium-team').val(),
            stadium_location: $('#modal-update-stadium-location').val(),
            stadium_capacity: $('#modal-update-stadium-capacity').val()
        };

       $.ajax({
           url: "/api/stadium/update",
           contentType: 'application/json',
           data: JSON.stringify(data),
           type: "POST",
           dataType : "json",
           success: function( json ) {
                if ( json.result ) {
                    $('#op-main-success-alert').show();
                    $('#modal-update-stadium').modal('hide');
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
    // Person Add
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

    // Person-Type Add
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

    // Penalty Add
    $('#modal-add-form-penalty').submit(function() {
        var user_data =
            {
                person_name: $('#modal-penalty-name').val(),
                penalty_given_date: $('#modal-penalty-given-date').val(),
                penalty_type: $('#modal-penalty-type').val()
            };

        $.ajax({
            url: "/api/penalty/add",
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
                    $('#add-new-penalty').modal('hide');
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

    // Penalty-Type Add
    $('#modal-add-penalty-type-form').submit(function() {
        var user_data = {
                penalty_type: $('#add-modal-penalty-type').val()
            };

        $.ajax({
            url: "/api/penalty/type/add",
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
                    $('#add-new-penalty-type').hide();
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

    // City Add
    $('#modal-city-add-form').submit(function() {
        var user_data =
            {
                city_name: $('#modal-city-name').val(),
                city_population: $('#modal-city-population').val()
            };

        $.ajax({
            url: "/api/city/add",
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

    // Country Add
    $('#modal-country-add-form').submit(function() {
        var user_data =
            {
                country_name: $('#modal-country-name').val(),
                country_population: $('#modal-country-population').val()
            };

        $.ajax({
            url: "/api/country/add",
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
                    $('#modal-country-add').modal('hide');
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

    // Match
    $('#modal-match-add-form').submit(function() {
        var user_data =
            {
                match_team_1: $('#modal-match-team1').val(),
                match_team_2: $('#modal-match-team2').val(),
                match_league: $('#modal-match-league').val(),
                match_stadium: $('#modal-match-stadium').val(),
                match_referee: $('#modal-match-referee').val(),
                match_date: $('#modal-match-date').val()
            };

        $.ajax({
            url: "/api/match/add",
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
                    $('#modal-country-add').modal('hide');
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

    // League Add
    $('#modal-league-add-form').submit(function() {
        var user_data =
            {
                league_name: $('#modal-league-name').val(),
                league_start_date: $('#modal-league-start-date').val(),
                league_country: $('#modal-league-country').val()
            };

        $.ajax({
            url: "/api/league/add",
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
                    $('#modal-league-add').modal('hide');
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

    // Player Add
    $('#modal-player-add-form').submit(function() {
        var user_data =
            {
                player_name: $('#modal-player-name').val(),
                player_goals: $('#modal-player-goals').val(),
                player_team: $('#modal-player-team').val()
            };

        $.ajax({
            url: "/api/player/add",
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
                    $('#modal-player-add').modal('hide');
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

    // Sponsorship Add
    $('#modal-add-form-sponsorship').submit(function() {
        var user_data =
            {
                sponsorship_name: $('#modal-sponsorship-name').val(),
                sponsorship_start_date: $('#modal-sponsorship-start-date').val(),
                sponsorship_league: $('#modal-sponsorship-league').val(),
                sponsorship_team: $('#modal-sponsorship-team').val(),
                sponsorship_person: $('#modal-sponsorship-person').val()
            };

        $.ajax({
            url: "/api/sponsorship/add",
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
                    $('#add-new-sponsorship').modal('hide');
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

    // Stadium Add
    $('#modal-add-form-stadium').submit(function() {
        var user_data =
            {
                stadium_name: $('#modal-stadium-name').val(),
                stadium_team: $('#modal-stadium-team').val(),
                stadium_location: $('#modal-stadium-location').val(),
                stadium_capacity: $('#modal-stadium-capacity').val()
            };

        $.ajax({
            url: "/api/stadium/add",
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
                    $('#add-new-stadium').modal('hide');
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

    // Team Add Form
    $('#modal-add-form-team').submit(function() {
        var user_data = {
                team_name: $('#modal-team-name').val(),
                team_couch: $('#modal-team-couch').val()
            };

        $.ajax({
            url: "/api/team/add",
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
                    $('#add-new-team').hide();
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

