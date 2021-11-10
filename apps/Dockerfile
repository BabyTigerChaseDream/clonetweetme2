#FROM python:3.8-slim-buster
# for mysql in comtainer,need to use 3.8 / slim-buster will not work
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /tweetme2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPY . .

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]