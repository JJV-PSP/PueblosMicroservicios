FROM python:alpine

COPY app.py requirements.txt /

RUN pip install -r requirements.txt

EXPOSE 5003

CMD ["python", "./app.py"]
