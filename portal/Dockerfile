# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /portal

# Install audio libs
RUN apt-get update && apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN apt-get install -y ffmpeg 

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .