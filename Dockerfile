# Use the official Ubuntu 22.04 base image
FROM ubuntu:22.04

# Set the timezone to Asia/Tokyo
RUN apt-get update
RUN apt-get install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# install app
RUN apt-get install git -y
RUN apt-get -y install ffmpeg
RUN apt install -y cron
RUN apt install -y vim

#ラズパイの場合、ubuntu上でinstallエラーとなる場合がある。
#無理やりinstallするため--break-system-packagesのオプションをつける。（ちゃんと稼働します）
RUN apt install python3-pip -y
RUN pip install mega.py
RUN pip install notion-client
RUN pip install pyinstaller