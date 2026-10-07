FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip &&  \
    pip isntall --no-cache-dir -r requirements.txt


CMD ["uvicorn","app.main:app","--host","0.0.0.0","8000"]