FROM python:alpine

COPY app.py municipio.json requirements.txt /

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]
