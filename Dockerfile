FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY comparison /comparison
COPY projects /projects
COPY manage.py /manage.py