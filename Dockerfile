FROM ubuntu:18.04

RUN apt-get update && apt-get install -y libglib2.0-0 \
	libnss3 \
	libgconf-2-4 \
	libfontconfig1 \
	sudo \
	python3 \
	python3-pip\
	vim\
	wget


COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN sudo apt install -y ./google-chrome-stable_current_amd64.deb

COPY . .

EXPOSE 5000
ENTRYPOINT ["/bin/bash"]

