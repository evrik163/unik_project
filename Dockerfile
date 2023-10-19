FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
EXPOSE 8000
RUN pip install --default-timeout=100 -r requirments.txt
ENTRYPOINT ["bash", "start.sh"]
