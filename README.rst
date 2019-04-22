=================
Django Greenfield
=================

Django Test project with support for Active Directory, pytest, Postgresql, ...


Install
-------

.. code:: bash

  $ docker-compose up
  $ docker-compose exec dc samba-tool user create nandersson Secret012 
  $ docker-compose exec dc samba-tool group add Staff
  $ docker-compose exec dc samba-tool group add Superusers 
  $ docker-compose exec dc samba-tool group addmembers Staff nandersson 
  $ docker-compose exec dc samba-tool group addmembers Superusers nandersson 
  $ docker-compose exec python python manage.py makemigrations widget
  $ docker-compose exec python python manage.py migrate
  $ docker-compose run -e DJANGO_SETTINGS_MODULE=greenfield.settings.testing --no-deps --rm python py.test

Test
----

.. code:: bash

  $ http POST http://localhost:8000/api/v1/widgets/ "Authorization: Token 29100fb235300217e2f8d8d13ede0e82aa4e5875" display_name="Some cool Widget"
