.. _dev-guide:

Developer Guide
===============

Database Design
---------------

Our database relations has been designated to be use power of relations as much as possible. All possible repeated data
amount has been reduced in order to reduce used storage amount. More detailed information has been explained by each group
member.

   .. figure:: er.png
      :align: center
      :scale: 50 %
      :alt: entity-relation diagram

      Entity-Relation Diagram for Database

Git Workflow
------------
Git workflow thorough development process has been visualized with open source software called gource.

   .. figure:: git.png
      :align: center
      :scale: 50 %
      :alt: git workflow

Code
----

For code structure, model-view-controller hierarchy has been used. Where model methods and control methods has been seperated.
For each entity a class has been created. These classes used as models which have done the database operations. Routes has been
connected to views and if user enters an input, entered data went through view to controller and then model. Also an API has been
created to made possible the abstract operations which is free from user interface. In reality, models has been designed as
API, thus it increases technical capabilities of our code. Each group member has been explained their parts in more detail.

.. toctree::

   member1
   member2
   member3
   member4

