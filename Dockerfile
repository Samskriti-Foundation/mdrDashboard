# Select a minimal base image with Python 3.11 (adjust if needed)
FROM python:3.11-slim-buster
MAINTAINER Narasimhan M.G. github.com/Naras
COPY ./mdrRestApi.py /usr/local/mdrDashboard/
COPY ./sqlDashboardQry.py /usr/local/mdrDashboard/
COPY ./db_credentials.yaml /usr/local/mdrDashboard/
COPY ./requirements.txt /usr/local/mdrDashboard/
EXPOSE 5000
WORKDIR /usr/local/mdrDashboard/
RUN pip3 install -r requirements.txt
CMD python mdrRestApi.py
