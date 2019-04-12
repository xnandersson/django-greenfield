FROM python:latest
MAINTAINER Niklas Andersson <niklas.andersson@openforce.se>
RUN apt-get update && apt-get install -yqq devscripts python3-dev libldap2-dev libsasl2-dev
RUN echo -e 'TLS_CACERT /etc/ssl/certs/ca-certificates.crt\nTLS_REQCERT ALLOW' >> /etc/ldap/ldap.conf
COPY ./src /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
