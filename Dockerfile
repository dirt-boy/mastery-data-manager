FROM ubuntu 18.04
FROM selenium/standalone-chrome
FROM python 3.8
FROM logstash



RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN apt update && apt-get install -y libglib2.0-0 \
	libnss3 \
	libgconf-2-4 \
	libfontconfig1

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "/app/course_util.py"]

