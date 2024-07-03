FROM python:3.6-alpine

WORKDIR /Flask-Clean-Blog

ADD . /Flask-Clean-Blog/

RUN pip install -r requirements.txt

ENV FLASK_APP=run.py

CMD [ "flask", "run" ]
