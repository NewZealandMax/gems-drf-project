FROM python:3.11-slim

WORKDIR /gems_project

COPY requirements.txt /gems_project/requirements.txt

RUN pip install -r /gems_project/requirements.txt --no-cache-dir

COPY gems_project/ /gems_project

CMD ["gunicorn", "gems_project.wsgi:application", "--bind", "0:8000" "--timeout 120"]
