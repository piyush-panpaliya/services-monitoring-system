FROM python:latest
WORKDIR /app
COPY . /app
# COPY  /etc/nginx/sites-enabled/* /app/nginx-sites-enabled/*
RUN pip install -r requirements.txt
EXPOSE 80
CMD python3 scrap.py && python3 app.py
