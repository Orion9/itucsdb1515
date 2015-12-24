Welcome to Dball's documentation!
=================================

:Team: ITUCSDB1515

:Members:

   * Oğuz Kerem Tural (150130125)
   * Umut Can Özyar (150130022)
   * Mert Şeker (150130119)
   * Furkan Akgün (150130106)

DBall Database Application is prepared for baseball, a branch of sport especially popular in American culture with more
than 300 hundred years of history. It can hold many of the statistical data that represents baseball as whole. It is
easy to use, simple yet also give much more flexibility than any other application. In other terms, it directly responds
to user. If user wants it complex it become like one. And more importantly it is multi functional and open source.

How to Install?
---------------
Just follow the following steps in order to install application.

    *   First go to the ``www.python.org`` and grab python (preferably version 3.4.3).
    *   Then install ``flask``, ``psycopg2``, ``passlib``  and ``requests`` packages through ``pip``.

        *   **PS.** You can use ``pip install flask psycopg2 passlib requests`` if ``pip`` is declared in your environment path.

    *   Then install PostgreSQL through ``www.postgresql.org``
    *   Setup database, then import ``init.sql`` file into database through recovery.
    *   Fire up ``server.py`` and you are ready to roll!


Contents:

.. toctree::
   :maxdepth: 1

   user/index
   developer/index
