FROM python:3.9-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install tcsh
RUN apt-get -y install gawk
COPY . /app/

RUN pip install -r requirements.txt
RUN uncompress /app/netphos-3.1.Linux.tar.Z && \
    tar -xvf /app/netphos-3.1.Linux.tar && \
    yes | cp -rf /app/ape.docker /app/ape-1.0/ape

RUN mkdir /app/temp
EXPOSE 8000
CMD ["python3", "main.py", "--port=8000"]

