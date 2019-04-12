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
