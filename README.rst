=================
Django Greenfield
=================

Django Test project with support for LDAP, pytest, Postgresql, ...


Prerequisites
-------------

.. code:: bash

  $ sudo apt-get install python3-venv devscripts python3-dev libldap2-dev libsasl2-dev ldap-utils docker.io
  $ sudo usermod -a -G docker nandersson
  $ docker pull ubuntu:latest
  

Install
-------

.. code:: bash

  $ python3 -m venv ~/venv3/django-greenfield
  $ source ~/venv3/django-greenfield/bin/activate
  $ pip install -U pip
  $ pip install -r requirements.txt
  $ src/manage.py migrate
  $ src/manage.py runserver
  $ echo TLS_REQCERT ALLOW >> ~/.ldaprc
  $ pytest
