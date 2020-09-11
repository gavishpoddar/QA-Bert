FROM python:3.7

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python model.py


EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080",  "--workers", "1", "--threads", "8", "app:app", "--timeout", "900"]