FROM python:3.8-slim-buster

WORKDIR /app
ADD *.py ./
ADD requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:4000", "main:app" ]
