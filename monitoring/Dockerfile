FROM python:3.10-slim

WORKDIR /app
COPY app.py .

RUN pip install flask psutil
RUN pip install flask requests

EXPOSE 5001

CMD ["python", "app.py"]
