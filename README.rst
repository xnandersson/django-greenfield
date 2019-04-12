=================
Django Greenfield
=================

Django Test project with support for LDAP, pytest, Postgresql, ...


Repositories
------------

.. code:: bash

  $ git clone git@github.com:xnandersson/django-greenfield.git
  $ git clone https://github.com/xnandersson/docker-slapd.git
  $ git clone https://github.com/xnandersson/docker-dc.git
  
Software Prerequisites
----------------------

.. code:: bash

  $ sudo apt-get install python3-venv devscripts python3-dev libldap2-dev libsasl2-dev ldap-utils docker.io postgresql-client-common postgresql-client-10 sqlitebrowser pgadmin3 -y
  
Pre-install
-----------

.. code:: bash

  $ mkdir -p ${HOME}/docker/volumes/postgres
  $ sudo docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v ${HOME}/docker/volumes/postgres:/var/lib/postgresql/data postgres
  $ psql -h localhost -U postgres -d postgres
  postgres=# create role greenfield with password 'Secret012' login;
  postgres=# create database greenfield;
  postgres=# grant all on database greenfield to greenfield;
  postgres=# \q
  $ PGPASSWORD="Secret012" psql -h 127.0.0.1 greenfield greenfield
  
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
