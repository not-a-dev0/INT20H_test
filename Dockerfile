FROM python:3.7
ADD . /app
WORKDIR /app
#EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
