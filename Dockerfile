FROM https
WORKDIR /app
COPY requirements.txt /app
COPY studybotproject /app
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt && \
    cd studybotproject
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "127.0.0.1:8000"]


