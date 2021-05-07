FROM ubuntu:18.04
MAINTAINER Seung 

RUN apt-get update
RUN apt-get install apache2 -y

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]