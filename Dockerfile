FROM python:3.11.3-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH=.
ENV DB_NAME=item

COPY ./ /app

RUN apt update && \
    apt install nmap -y && \
    pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["python", "src/main.py"]
