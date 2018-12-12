FROM python:3.6.7
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

EXPOSE 9999
