FROM python:alpine

COPY app.py demo.json requirements.txt /

RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["python", "./app.py"]
