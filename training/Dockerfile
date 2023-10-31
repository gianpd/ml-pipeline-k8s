FROM python:3.11-slim-buster
WORKDIR /usr/app
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

COPY ./app/** .
ENTRYPOINT ["python3", "main.py"]