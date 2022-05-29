FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r /app/requirement.txt

EXPOSE 5000
CMD ["python3", "/app/app/utilApp.py"]