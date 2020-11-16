FROM python:3.9.0-alpine3.12
WORKDIR /ExamenU5
RUN apk add --no-cache --upgrade bash
COPY requeriments.txt .
RUN pip install -r requeriments.txt
COPY src/ .
CMD ["python", "./ExamenU5.py"]