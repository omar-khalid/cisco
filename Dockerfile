FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY movie_rating.py .
COPY ./startup.sh /

ENTRYPOINT ["./startup.sh"]

CMD []

