FROM python:3.9.1

RUN apt-get update && apt-get update && apt-get install -y wget apt-utils


RUN wget -P /tmp https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt install -y /tmp/google-chrome-stable_current_amd64.deb

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


ENTRYPOINT ["bash"]
