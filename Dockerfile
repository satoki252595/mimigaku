# Use the official Ubuntu 22.04 base image
FROM ubuntu:22.04

# Set the timezone to Asia/Tokyo
RUN apt-get update
RUN apt-get install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# install app
RUN apt-get install git -y
RUN apt-get -y install ffmpeg

RUN apt install python3-pip -y
RUN pip install mega.py
RUN pip install notion-client

