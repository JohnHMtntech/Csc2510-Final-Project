FROM python:3.14-slim

COPY . /app
WORKDIR /app

#Download libraries
RUN pip install pygame-ce

#Run code
CMD ["python3", "./graphics.py"]