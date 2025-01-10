
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY app/flask_log_vote_server.py /app/flask_log_vote_server.py

ENV FLASK_APP=flask_log_vote_server.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
