FROM selenium/standalone-chrome
FROM python:3.8

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN apt update && apt-get install -y libglib2.0-0 \
	libnss3 \
	libgconf-2-4 \
	libfontconfig1

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/course_util.py"]

