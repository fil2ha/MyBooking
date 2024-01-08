FROM python:3.10

COPY requirements.txt /temp/requirements.txt
COPY booking /booking
WORKDIR /booking
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

