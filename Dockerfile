FROM python:3.11

RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
EXPOSE 8000