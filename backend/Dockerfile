FROM python:3.12.3

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

VOLUME ["/backend/static", "/backend/media"]

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN ["chmod", "+x", "./entrypoint.sh"]

ENTRYPOINT ["./entrypoint.sh"]
