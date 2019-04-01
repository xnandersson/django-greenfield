=================
Django Greenfield
=================

Django Test project with support for LDAP, pytest, Postgresql, ...


Software Prerequisites
----------------------

.. code:: bash

  $ sudo apt-get install python3-venv devscripts python3-dev libldap2-dev libsasl2-dev ldap-utils docker.io postgresql-client-common postgresql-client-10 -y
  $ sudo usermod -a -G docker nandersson
  $ docker pull ubuntu:latest
  
Pre-install
-----------

.. code:: bash

  $ sudo docker pull postgres
  $ mkdir -p ${HOME}/docker/volumes/postgres
  $ sudo docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v ${HOME}/docker/volumes/postgres:/var/lib/postgresql/data postgres
  $ psql -h localhost -U postgres -d postgres
  
Install
-------

.. code:: bash

  $ python3 -m venv ~/venv3/django-greenfield
  $ source ~/venv3/django-greenfield/bin/activate
  $ pip install -U pip
  $ pip install -r src/requirements.txt
  $ src/manage.py migrate
  $ src/manage.py createsuperuser
  $ src/manage.py runserver
  $ echo TLS_REQCERT ALLOW >> ~/.ldaprc
  $ pytest
