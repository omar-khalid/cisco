FROM python:3

COPY requirements.txt movie_rating.py startup.sh ./
RUN pip install -r requirements.txt

ENTRYPOINT ["./startup.sh"]

CMD []

