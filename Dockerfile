FROM python:3.10.10-slim-buster

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

COPY app .

RUN pip install -r requirements.txt

CMD ["bash", "entrypoint.sh"]
