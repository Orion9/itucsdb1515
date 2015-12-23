Parts Implemented by Furkan Akgün
================================

Change Log
----------

When you first enter the site, you will realize that there is a column showing the last five operations done in the site.
When an authenticated user perform an operation, last five operations always be showing up in main page. If that is the
first time user entered the site, by checking both columns in the home page and examining last changes user can get an
idea of the website. On the other hand if it is not user's first time, then instead of checking all tables to see what changed;
user can simply look on the last changes column.

    .. figure:: furkan_pics/last_changes_main.png
       :align: center
       :scale: 50%
       :alt: last changes

       Last Changes Column in Home Page

Change Log serves two main ideas; to track down which operations are done and by whom, and by some chance if database
operations fails as a means of debugging. In the home page we represent only the last five changes, but in manager screen
all logs are stored.

    .. figure:: furkan_pics/change_log_main.png
       :align: center
       :scale: 50%
       :alt: change log

       All Stored Log Data

As can seen in the above figure, logs are all divided into 3 different columns; first column to explain what is done,
second to tell by whom and the third for date of the operation. In the main change log it is easy to differentiate users
from the description because table structure make their positions clear. But in the home page in last changes column,
in some cases it may not be easy to see user in first glance. So to emphasize some keywords in log like user, we used bold
font for users.

Country
-------

All country data are stored in database.So we have basically a front page to represent or change this data. First page is simply
on /country route and its purpose to represent data we have in an elegant way and providing some functionality.

    .. figure:: furkan_pics/country_front_page.png
       :align: center
       :scale: 50%
       :alt: country front page

        Front Page For Countries

As can seen in the above figure, data simply divided into 3 columns; country name, country's capital and the population.
Also table is striped table meaning that if you have your cursor over a row, that row will be focused and will be easy to see.
There are location markers next to city and country names, as you can guess by clicking those icons user can see location
of clicked name on GoogleMaps Api.

    .. figure:: furkan_pics/country_location.png
       :align: center
       :scale: 50%
       :alt: browse location

       Country Locations

In this example I have clicked on Paris and the results can be seen as in the figure above. Right after clicking the location
marker, a modal with location map shows up by taking all the focus.
Also at the top of the table you can see "Manage" button. By clicking this button, if user have sufficient permission, user
will be directed to manager page for countries where he/she can change data.

Second page for both representing and changing data for countries is on the /manager/country route
and only users with sufficient permissions can locate the page. In this page, all data represented in data table structure.
Also any columns for country such as id are shown here while it was not showing in the front page.

    .. figure:: furkan_pics/country_manager.png
       :aling: center
       :scale: 50%
       :alt: country manager screen

       Country Manager Page

On the top left side of the table you can select how many records to show in a single page. And on the top right side of the table
you can search for any records. By clicking on the column name you can sort all records by the clicked column.

And finally the last three buttons in the bottom of the page are add, update and delete buttons respectively.

Add Operation
+++++++++++++

By clicking the "Add New Data" button on the bottom of the page, a modal shows up prompting data for new record.

    .. figure:: furkan_pics/add_country.png
       :align: center
       :alt: Add Country

       Country Add Screen

First is country name which is simply a textbox and user can enter a country name in mind. Second is city name; users can
only select cities currently on the database which are available in the selection. Third is population and users can enter
an integer value.
Right after completing the input and clicking the "Submit" button at the buttom of page. If there is no problem in backend
new country data will be added to database and now can be seen in both front and manager pages.

Update Operation
++++++++++++++++

By clicking the "Update Selected Data" button a modal will show up if the user have selected only one row. If selected row count
exceeds one, then right after user clicked update button an error will show up on the top of table warning users about number
of selected items.

    .. figure:: furkan_pics/county_update_manyrows.png
       :align: center
       :scale: 50%
       :alt: can not update many rows at once

       A Warning Appears if User Tries to Update Many Rows in an Operation

After user selected only one row and clicked update button a modal for updating data will show up.

    .. figure:: furkan_pics/country_update.png
       :align: center
       :alt: country update screen

       Country Update Screen

Right after user fill the inputs and submit the form ,if nothing prevents in the backend, selected row of country table
will be updated. After update operation all links of previous data also be changed by the new data.

Delete Operation
++++++++++++++++

By clicking the "Delete Selected Row(s)" button user can delete either one entry or multiple entries. After user selected
the rows he/she wish to delete, clicking the button will delete all selected rows from the table.

Match
-----

As like the country, match table also have two different pages on purpose. One again for to represent data in an elegant way,
the other for changing the data. First page is to represent data and any user can locate this page on route /matches.

    .. figure:: furkan_pics/match_front.png
       :align: center
       :scale: 50%
       :alt: match page

       Front Match Page

As can seen in the above figure, data is represented in a table structure and have several columns which are date, results,
referee and stadium. Date, simply as the name says, shows the date when the match took place and formatted as D/M/Y. Results
column shows teams and their scores with scores emphasized. And so stadium shows which stadium match took place and referee
shows who was the referee in the match.

After user clicked "Manage Button" on the top of table, user will be directed to /manager/matches page if he/she have
sufficient permission.

Second page is for both representation and modifying data and can be accessed only by authenticated users.

    .. figure:: furkan_pics/matches_manager.png
       :align: center
       :scale: 50%
       :alt: manager match page

       Manager Page For Matches

Add Operation
+++++++++++++

Just like in the country page, when clicking "Add New Data" a modal shows up and asks for data for entry to be added.

    .. figure:: furkan_pics/matches_add.png
       :align: center
       :alt: add new match

       Add Screen for Matches

Here you can choose two teams registered in database in dropdown menus and set score values for each of them. Score value
must be between 0 and 100. Next choose a stadium from database and assign it to this match. You can also select a referee
and specify date of the match in this add screen.

Update Operation
++++++++++++++++

After clicking "Update Data" Button after selection row to be updated, a modal shows up asks for user to enter new data.
In every page, just like in country page, user should select only one row to update. If user, by any change, try to update
two or more row at the same time, a warning message will be created.

    .. figure:: furkan_pics/matches_update.png
       :align: center
       :alt: update match

       Update Screen for Matches

You can simply change any value of the match without damaging integrity of database.

Delete Operation
++++++++++++++++

Just like in country page, you can select one or multiple entries and then hit delete button to delete them from the
database.

League
------

All league data are stored in database. League data just like the other tables have two pages with different purposes;
one for representing the data in a way appropriate to content and the other for editing data.

    .. figure:: furkan_pics/league_front.png
       :align: center
       :scale: 50%
       :alt: league front page

       League Front Page

In this page, user can see all the leagues registered in database. User can see a league's country and start date. What's
more is that by clicking the "Leaderboard" button, user can access leaderboard for that league easily.

    .. figure:: furkan_pics/league_front_collapsed.png
       :align: center
       :scale: 50%
       :alt: league leaderboards

       League Leaderboards

Manager page of leagues is also identical to the other class manager pages. All data are in datatable and ready to modify.

    .. figure:: furkan_pics/league_manager.png
       :align: center
       :scale: 50%
       :alt: league manager

       Manager Page for League

Add Operation
+++++++++++++

Just like previous classes, after clicking add button a modal for league shows up and prompts for entry. After submitting
new entry will be added to the database.

    .. figure:: furkan_pics/league_add.png
       :align: center
       :alt: league add

       Add Screen for League

Here user can name the league anything he wants and can select a registered country from the database in dropdown menu.
Also user can specify start date of the league.

Update Operation
++++++++++++++++

User first select one row to be updated by clicking on rows. However only one row at a time allowed to be updated, meaning
if user ever try to update two or more selected items, a warning will appear in top of the table just like in country and match
page.

    .. figure:: furkan_pics/league_update.png
       :align: center
       :alt: league update

       Update Screen for League

Delete Operation
++++++++++++++++

User must first select the rows he/she wish to delete. After selecting the one or multiple rows to be deleted just hitting
delete button will delete all selected data from the database.