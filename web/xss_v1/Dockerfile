FROM evpavel/slimerjs-alpine:latest

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

COPY . /app
WORKDIR /app    
    
RUN pip install -r requirements.txt

#ENTRYPOINT ["python"]
#CMD ["app.py"]