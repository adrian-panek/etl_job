FROM python:3.10.15-alpine3.20
WORKDIR /etl
COPY ./requirements.txt /etl
RUN pip install -r requirements.txt
RUN mkdir /etl/scripts
ADD ./scripts ./scripts
ENTRYPOINT ["python3", "scripts/python/main.py"]