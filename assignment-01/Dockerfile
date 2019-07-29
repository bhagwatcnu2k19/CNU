FROM python:3.6
EXPOSE 5000
ENV FLASK_APP src.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "run"]