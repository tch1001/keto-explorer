FROM python:3.9-slim-buster 
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y libsqlite3-dev
RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
COPY . /app
COPY .env /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]
