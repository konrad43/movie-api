FROM python:3.6

ENV PYTHONBUFFERED 1

RUN mkdir /k_bonder
WORKDIR /k_bonder
COPY requirements.txt /k_bonder
RUN pip install -r requirements.txt
COPY . /k_bonder/