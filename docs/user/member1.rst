Parts Implemented by Oğuz Kerem Tural
=====================================

Main Area
---------

Upon entering the application, user faces with this screen. It contains a navigation bar on top, a search box and
two columns. Search box is not yet active. Still user can search each table from their singular views. From top
navigation bar user can move across table views and login if it is not yet logged in. Also from right side column,
user can be able to see latest changes on records have done by registered users.

   .. figure:: oguz_pics/main_area.png
      :scale: 50 %
      :alt: main screen

      Main screen of the application.

Navigation Bar
++++++++++++++

From this area users can move thorough table views of front area. Also from right corner, where a door symbol seen,
user can login to the application. If user already logged in, it can enter management area using drop down menu which
replaces login button after log in operation. Using drop down menu user can advance between management and front pages
and sign out when it is needed.

   .. figure:: oguz_pics/navbar_notlogin.png
      :scale: 50 %
      :alt: navbar without login

      Navigation bar before user logs in.

   .. figure:: oguz_pics/navbar.png
      :scale: 50 %
      :alt: navbar with login

      Navigation bar after user logs in

   .. figure:: oguz_pics/navbar_user_menu.png
      :scale: 85 %
      :alt: navbar use_menu

      This menu will appears when user logs in, instead of login button.

User System
-----------
User system in application is very basic and an abstract system that aims to prevent anonymous changes could have been done
to database records. Every registered user has right to add, update or delete records where as unregistered users can only
view, search and filter the records. Both user login and register operations are done using an Auth API service that has
been provided by application itself. For further information about API please reference to developer guide.

Login Using Interface
+++++++++++++++++++++

To login using interface, user should click the button provided in navigation bar's top right corner with the door symbol on it.
After click, a modal window will be shown which provides user name and password fields to user for log in operation.

   .. figure:: oguz_pics/user_login.png
      :scale: 50 %
      :alt: navbar login

      Login modal screen.

If user enters wrong credentials, an error message will appear and warns user about wrong credentials.

   .. figure:: oguz_pics/user_login_error.png
      :scale: 50 %
      :alt: navbar login error

      The message that appears when user enters wrong credentials.

Management Area
---------------
Registered users have privileges to change the records that stored in database. After user logged in, it can redirect here
using drop down user menu in navigation bar. In same way, it can go back to front area using drop down menu in navigation bar.
In here user greeted with change history again. But difference between the main screen change log and manager screen change log is
in manager screen user can be able to see all changes has been done from beginning of the application. User can move to the
management areas for different tables from sidebar.

   .. figure:: oguz_pics/manager_main_area.png
      :scale: 50 %
      :alt: manager main

      Manager main screen.

Sidebar
+++++++
From this section, user can navigate through different tables easily. Active page will be highlighted.

   .. figure:: oguz_pics/manager_sidebar.png
      :scale: 50 %
      :alt: manager sidebar

      Side navigation bar in management area.

.. _people-rec:

People Records
--------------
In application each person stored in people table. From front view both unregistered and registered user can see the
view front page.

   .. figure:: oguz_pics/front_people.png
      :scale: 50 %
      :alt: people front

      Front view for people table.

User can search records that are listed in table. To search user should just type keywords into search box in right corner
of the table. Also user can order tables by clicking the header of column whose elements would order the table accordingly.
User can order table in ascending or descending order.

   .. figure:: oguz_pics/search_people.png
      :scale: 50 %
      :alt: people search

      Searching in people table.

Also user can change number of elements that are shown in pages.

   .. figure:: oguz_pics/number_of_list.png
      :scale: 50 %
      :alt: people list

      Number of elements that are going to shown in page.

From top button right next to title user can advance into management area. If user not logged in it would give an error
and asks user to login.

   .. figure:: oguz_pics/error_manage_not_login.png
      :scale: 50 %
      :alt: manager login error

      Error that occurs when unregistered user tries to advance in manager area.

When user advances into management area, three button would appear in the bottom of the table. First of them is for adding
operation, second of them is for update and the last one is for delete operation.

   .. figure:: oguz_pics/people_buttons.png
      :scale: 50 %
      :alt: people buttons

      Buttons that appear in management area.

If operations are successful a success message will appear on top of the table, if not then an error message will appear.

   .. figure:: oguz_pics/op_bam.png
      :scale: 50 %
      :alt: success message

      Success message.

   .. figure:: oguz_pics/op_error.png
      :scale: 50 %
      :alt: error message

      Error message.

Add Operation
+++++++++++++
User can add both person information and person type. Still be warned, person types cannot be deleted from database so
add them wisely and only when its necessary.

From ''Add New Data'' button, open drop down menu. After that user can select either to add new person or person type.
When clicked the selected button, a modal which would provide inputs will appear.

    * **PS.** *If you are not using Chromium-based browser please enter the date in ISO format (YYYY-mm-dd).*

   .. figure:: oguz_pics/add_person.png
      :scale: 50 %
      :alt: people buttons

      Add person modal.

   .. figure:: oguz_pics/people_type_add.png
      :scale: 50 %
      :alt: people buttons

      Add person type modal.

User should fill all necessary inputs. If it skips any of them a warning will appear and prevent user to send data.

   .. figure:: oguz_pics/required_error.png
      :scale: 50 %
      :alt: user warning

      User warning.

Update Operation
++++++++++++++++
User can update records easily first selecting which record will be updated and then clicking ''Update Selected Row'' button.
Still, only one record can be updated at time. If user selects more record and hits the update button an error message different from
other will be appear.

   .. figure:: oguz_pics/selection_many_error.png
      :scale: 50 %
      :alt: update selection error

      Error which appears when user select many records to update.


   .. figure:: oguz_pics/row_selection.png
      :scale: 50 %
      :alt: row selection

      Selecting a row.

After selecting one record, user can hit update button. When user clicks the update button a modal which provides
pre-filled inputs would appear. After that user can change any value as it would like.

   .. figure:: oguz_pics/update_person.png
      :scale: 50 %
      :alt: people update

      Person update modal.

Delete Operation
++++++++++++++++

User can delete multiple records at one time. User only needs to select which records to be deleted and hit the
delete button. If operation successful the success message will appear and page will reload.

Penalty Records
---------------
In penalty records most of the table functionality are the same as people table since all tables derived from a generic
table design. Hence, user can search, filter and move across table pages in same way. For those operations please refer to
:ref:`people-rec`.

   .. figure:: oguz_pics/penalty_main.png
      :scale: 50 %
      :alt: penalty main

      Penalty records table.

Add Operation
+++++++++++++
When user clicks the ''Add New Data'' button a drop down similar in people records will appear. From there user can add
either a new penalty record or penalty type record.
    * **PS.** *Beware penalty type records cannot be deleted*
    * **PPS.** *If user not using Chromium-based browser, it should enter the date in ISO format (YYYY-mm-dd).*

   .. figure:: oguz_pics/penalty_add.png
      :scale: 50 %
      :alt: penalty add

      Penalty add modal.

   .. figure:: oguz_pics/penalty_type.png
      :scale: 50 %
      :alt: penalty type add

      Penalty type add modal.

Update Operation
++++++++++++++++
User can update one record at a time. If more rows selected, user will encounter with an error same as in people records.
Again user should click ''Update Selected Row'' button to reveal update modal which provides necessary inputs for operation.

   .. figure:: oguz_pics/update_penalty.png
      :scale: 50 %
      :alt: penalty update

      Penalty update modal.

Delete Operation
++++++++++++++++
User can delete selected rows. First it should select every rows that need to be deleted then it should hit
''Delete Selected Row(s)'' button. If operation successful, success message will appear and page will be reloaded.

Popularity Records
------------------
Again in same fashion, popularity records also uses generic table view for user end. User can do all operations that can
be done in people record. For further information please refer to :ref:`people-rec`.

   .. figure:: oguz_pics/popularity_main.png
      :scale: 50 %
      :alt: popularity main

      Popularity main screen.

Add Operation
+++++++++++++
When user clicks the ''Add New Data'' button this time add modal directly appears and provides input for record. User
should fill all necessary input or a warning will warn the user and prevent submitting info.

   .. figure:: oguz_pics/popularity_add.png
      :scale: 50 %
      :alt: popularity add

      Popularity add modal.

Update Operation
++++++++++++++++
Again in here, user can update one record at a time. If more rows selected, user will encounter with an error same as in people records.
Again user should click ''Update Selected Row'' button to reveal update modal which provides necessary inputs for operation.

   .. figure:: oguz_pics/popularity_update.png
      :scale: 50 %
      :alt: popularity update

      Popularity update modal.

Delete Operation
++++++++++++++++
User can delete selected rows. First it should select every rows that need to be deleted then it should hit
''Delete Selected Row(s)'' button. If operation successful, success message will appear and page will be reloaded.

City Records
------------
In city records, user again can do the same operations as described in people records section. For more information about
that operations please refer to :ref:`people-rec`. Additionally, user can see the location of city on map using
''Show Location'' button. When user hits this button after selecting a city record, a extra modal which contains a map and a marker that show location
will appear. Still, user can only see one location at a time. If it selects more an error will appear.

   .. figure:: oguz_pics/city_main.png
      :scale: 50 %
      :alt: city main

      City main screen.

   .. figure:: oguz_pics/city_location.png
      :scale: 50 %
      :alt: city location

      City location modal.

Add Operation
+++++++++++++
Again as it before, when user clicks ''Add New Data'' button, a modal which provides necessary inputs for record will
appear.

   .. figure:: oguz_pics/city_add.png
      :scale: 50 %
      :alt: city add

      City add modal.

Update Operation
++++++++++++++++
User can update one record at a time. If more rows selected, user will encounter with an error same as in people records.
Again user should click ''Update Selected Row'' button to reveal update modal which provides necessary inputs for operation.

   .. figure:: oguz_pics/city_update.png
      :scale: 50 %
      :alt: city update

      City update modal.

Delete Operation
++++++++++++++++
User can delete selected rows. First it should select every rows that need to be deleted then it should hit
''Delete Selected Row(s)'' button. If operation successful, success message will appear and page will be reloaded.