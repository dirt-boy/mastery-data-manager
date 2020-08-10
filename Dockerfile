FROM python:3.8

RUN apt-get update && apt-get install -y libglib2.0-0 \
	libnss3 \
	libgconf-2-4 \
	libfontconfig1 \
	sudo

RUN sudo mkdir /app
WORKDIR sudo /app
ADD . /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "/app/course_util.py"]

