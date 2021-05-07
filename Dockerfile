FROM sjoh0704/django:latest
MAINTAINER seung
RUN pip3 install django
WORKDIR /usr/src/app
COPY . .
WORKDIR ./project
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
