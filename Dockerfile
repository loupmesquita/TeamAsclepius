FROM ubuntu:latest

COPY . .

RUN apt-get upgrade
RUN apt-get update

RUN apt-get -y install python3-opencv
RUN apt-get -y install python3-pip

RUN pip3 install pandas
RUN pip3 install requests

CMD python3 test.py