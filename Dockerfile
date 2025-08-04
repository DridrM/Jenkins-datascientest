# Dockerfile to build a flask app

FROM python:3.8-slim-buster

WORKDIR /usr/ 

COPY ./requirements.txt /usr/requirements.txt
RUN pip install -r /usr/requirements.txt

COPY . .

CMD ["python", "-m" , "flask", "run"]