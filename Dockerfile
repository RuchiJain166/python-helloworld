FROM python:3.8-alpine

RUN mkdir /app

ADD . /app

WORKDIR /app

ENTRYPOINT ["/bin/bash"]

CMD ["python", "app.py"]
