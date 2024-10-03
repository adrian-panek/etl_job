FROM python:3.10.15-alpine3.20
WORKDIR /etl
COPY ./requirements.txt /etl
RUN pip install -r requirements.txt
COPY . /etl
ENTRYPOINT ["python3", "main.py"]