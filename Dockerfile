FROM ubuntu:18.04

RUN apt-get update && apt-get install -y libglib2.0-0 \
	libnss3 \
	libgconf-2-4 \
	libfontconfig1 \
	sudo \
	python3 \
	python3-pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
ENTRYPOINT ["python3", "/app/course_util.py"]

