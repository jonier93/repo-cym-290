FROM python:3.9.16

WORKDIR /project

COPY . /project

RUN pip install -r requeriments.txt

CMD ["python", "server.py"]