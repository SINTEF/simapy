# run stage
FROM python:3.8-slim

WORKDIR /dmtpy

COPY src src
COPY requirements.txt .
COPY requirements-dev.txt .
COPY setup.py .
COPY README.md .

RUN pip install -r requirements-dev.txt -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

RUN pylint src/simapy --errors-only 
RUN pylint src/marmo --errors-only 
RUN pylint src/sima --errors-only