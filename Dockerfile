FROM python:3.11-bullseye

RUN mkdir /app/

COPY . /app/

EXPOSE 80

RUN pip install -r /app/requirements.txt

CMD ["python3", "/app/guesser.py"]