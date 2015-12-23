Parts Implemented by Umut Can Ozyar
===================================

.. _sponsorship:

Sponsorships
------------
The sponsorships data is stored in the database. Using the navigation bar located at the top of the front page sponsorships
table can be accessed.

    .. figure:: umut_pics/navigation_front.png
       :align: center
       :scale: 50%
       :alt: navigation front

       Navigation Bar For Selecting Pages

This table displays the sponsorships data in the database.

    .. figure:: umut_pics/sponsorship_front.png
       :align: center
       :scale: 50%
       :alt: sponsorship front page

       Front Page For Sponsorships

Several alterations can be made by the user to change the way the data is displayed on the table. The amount of entries
desired to be shown can be changed from the drop down list located at the top left of the table. The selected number
corresponds to the amount of rows displayed by the table. In case the selected number exceeds the amount of sponsorships
data, only the existing data will be displayed with no empty rows.

    .. figure:: umut_pics/table_show.png
       :align: center
       :scale: 50%
       :alt: show entity amount

       Menu for Shown Entity Amount Selection

There are also page control buttons located at the bottom right side of the table. These buttons are used to navigate
through different table pages if perchance there are more data in the database than the amount selected to be shown.

    .. figure:: umut_pics/table_next.png
       :align: center
       :scale: 50%
       :alt: table navigation

       Buttons For Table Navigation

The ordering of the data throughout the table can be changed by clicking on the sort buttons located at each table header.
This feature allows user to sort the data depending on various attributes of the table in descending or ascending order.

    .. figure:: umut_pics/table_sort.png
       :align: center
       :scale: 50%
       :alt: table sort

       Sorting Table

If there is no data in the database about sponsorships, "No data available in table" message is displayed on the
table to notify the user.

    .. figure:: umut_pics/table_no_data.png
       :align: center
       :scale: 50%
       :alt: empty table

       Empty Table

The manage button located on top of the table directs to user to the manager of the sponsorship table. This page is limited
for registered users only. Guest users will be notified to login using the login button located at the top right side of
the page.

    .. figure:: umut_pics/alert_login.png
       :align: center
       :scale: 50%
       :alt: login alert

       Login Alert

Manager page allows user to add new data, update existing data or delete existing data.

    .. figure:: umut_pics/sponsorship_manager.png
       :align: center
       :scale: 50%
       :alt: sponsorship manager

       Manager For Sponsorships

.. _sponsorship-add:

Add Sponsorship
+++++++++++++++
"Add New Data" button allows the user to add a new sponsorship for league, team and person entities in any combination.
Then a modal for adding new data will appear. This modal contains several fields corresponding to different attributes
of the table.

    .. figure:: umut_pics/sponsorship_add.png
       :align: center
       :scale: 50%
       :alt: sponsorship add

       Modal For Adding Sponsorships

First input field is for the name of the sponsor. The second field brings out a calender for sponsorship start date selection.
Third field is for selecting the sponsored league. Fourth field is for selecting the sponsored team and the last field is
for the sponsored person. Some of the last three fields can be left blank as a sponsor doesn't have to sponsor a league,
a team and a person at the same time. After the necessary fields are filled submit button is used to add the data to the
table.

Some of these fields like the name and the start date cannot be left blank and will warn the user if submit button is
clicked without filling these fields.

    .. figure:: umut_pics/validation.png
       :align: center
       :scale: 50%
       :alt: validation

       Validation For Required Fields

Alerts will appear on top of the table to notify the user about the outcome of the add operation. This can either be a
success message with a green background which means that data is added to the database successfully or it can be a failure
message with a red background which means that a problem has occurred and the operation is unsuccessful.

    .. figure:: umut_pics/alert_success.png
       :align: center
       :scale: 50%
       :alt: success alert

       Success Alert

    .. figure:: umut_pics/alert_failure.png
       :align: center
       :scale: 50%
       :alt: failure alert

       Failure Alert

Update Sponsorship
++++++++++++++++++
"Update Selected Row" button allows the user to update a sponsorship entity on the table. If a row is not selected or
multiple rows are selected, an error message notifies the user to select a single row.

If a single row is selected a modal for updating data will appear. This modal contains several fields corresponding to
different attributes of the table filled with the existing data.

    .. figure:: umut_pics/sponsorship_update.png
       :align: center
       :scale: 50%
       :alt: sponsorship update

       Modal For Updating Sponsorships

Several attributes can be updated using this modal at the same time. Some fields like the name and start date will still
be required to be filled. Submit button will update the data on the database.

Please refer to :ref:`sponsorship-add` for more detail about the fields and all encountered alerts.



Delete Sponsorship
++++++++++++++++++
"Delete Selected Row(s)" button allows the user to delete sponsorship entities from the table. At least one row has to be
selected to perform this operation.

    .. figure:: umut_pics/sponsorship_delete.png
       :align: center
       :scale: 50%
       :alt: sponsorship delete

       Delete Operation For Sponsorships


Team Statistics
---------------
The team statistics data is stored in the database. Using the navigation bar located at the top of the front page team
statistics table can be accessed. This table displays the sponsorships data in the database.

    .. figure:: umut_pics/team_stat_front.png
       :align: center
       :scale: 50%
       :alt: team_stat front page

       Front Page For Team Statistics

The manage button located on top of the table directs to user to the manager of the team statistics table. This page is
limited for registered users only. Manager page allows user to add new data, update existing data or delete existing data.

    .. figure:: umut_pics/team_stat_manager.png
       :align: center
       :scale: 50%
       :alt: team_stat manager

       Manager For Team Statistics

.. _team_stat-add:

Add Team Statistics
+++++++++++++++++++
"Add New Data" button allows the user to add team statistics for an existing team. Then a modal for adding new data will
appear. This modal contains several fields corresponding to different attributes of the table. Wins, draws and losses are
automatically calculated according to the matches data.

    .. figure:: umut_pics/team_stat_add.png
       :align: center
       :scale: 50%
       :alt: team_stats add

       Modal For Adding Team Statistics

First input field is a drop down menu for team selection. The rest of the fields are inputs for batting runs, batting hits,
pitching saves respectively. After the necessary fields are filled submit button is used to add the data to the
table.

Please refer to :ref:`sponsorship-add` for instructions about validation or alerts, and :ref:`sponsorship` for navigation.

Update Team Statistics
++++++++++++++++++++++
"Update Selected Row" button allows the user to update a team statistics entity on the table. If a row is not selected or
multiple rows are selected, an error message notifies the user to select a single row.

If a single row is selected a modal for updating data will appear. This modal contains several fields corresponding to
different attributes of the table filled with the existing data.

    .. figure:: umut_pics/team_stat_update.png
       :align: center
       :scale: 50%
       :alt: team_stats update

       Modal For Updating Team Statistics

Several attributes can be updated using this modal at the same time. Some fields like hits, runs and saves date will still
be required to be filled. Submit button will update the data on the database.

Please refer to :ref:`team_stat-add` for more detail about the fields and :ref:`sponsorship-add` for all encountered alerts.

Delete Team Statistics
++++++++++++++++++++++
"Delete Selected Row(s)" button allows the user to delete team statistics entities from the table. At least one row has
to be selected to perform this operation.

    .. figure:: umut_pics/team_stat_delete.png
       :align: center
       :scale: 50%
       :alt: team_stats delete

       Delete Operation For Team Statistics

Stadiums
--------
The stadium data is stored in the database. Using the navigation bar located at the top of the front page stadiums table
can be accessed. This table displays the stadiums data in the database.

    .. figure:: umut_pics/stadium_front.png
       :align: center
       :scale: 50%
       :alt: stadium front page

       Front Page For Stadiums

The manage button located on top of the table directs to user to the manager of the stadium table. This page is limited
for registered users only. Manager page allows user to add new data, update existing data or delete existing data.

    .. figure:: umut_pics/stadium_manager.png
       :align: center
       :scale: 50%
       :alt: stadium manager

       Manager For Stadiums

.. _stadium-add:

Add Stadium
+++++++++++
"Add New Data" button allows the user to add a new stadium for an existing team. Then a modal for adding new data will
appear. This modal contains several fields corresponding to different attributes of the table.

    .. figure:: umut_pics/stadium_add.png
       :align: center
       :scale: 50%
       :alt: stadiums add

       Modal For Adding Stadiums

First input field is the name of the stadium. Second input field is a drop down menu for team selection. Third input field
is another drop down menu for location selection which indicates the city the stadium is located in. The last field is a
numerical value representing the capacity of the stadium. After the necessary fields are filled submit button is used to
add the data to the table.

Please refer to :ref:`sponsorship-add` for instructions about validation or alerts, and :ref:`sponsorship` for navigation.

Update Stadium
++++++++++++++
"Update Selected Row" button allows the user to update a stadium entity on the table. If a row is not selected or
multiple rows are selected, an error message notifies the user to select a single row.

If a single row is selected a modal for updating data will appear. This modal contains several fields corresponding to
different attributes of the table filled with the existing data.

    .. figure:: umut_pics/stadium_update.png
       :align: center
       :scale: 50%
       :alt: stadiums update

       Modal For Updating Stadiums

Several attributes can be updated using this modal at the same time. None of the fields can be left blank. Submit button
 will update the data on the database.

Please refer to :ref:`stadium-add` for more detail about the fields and :ref:`sponsorship-add` for all encountered alerts.

Delete Stadium
++++++++++++++
"Delete Selected Row(s)" button allows the user to delete stadium entities from the table. At least one row has to be
selected to perform this operation.

    .. figure:: umut_pics/stadium_delete.png
       :align: center
       :scale: 50%
       :alt: stadium delete

       Delete Operation For Stadiums