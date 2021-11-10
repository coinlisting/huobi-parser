FROM python:3.10.0

WORKDIR /news

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . /news

CMD ["python", "/news/index.py"]