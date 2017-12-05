FROM evpavel/slimerjs-alpine:latest

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

COPY . /app
WORKDIR /app    
    
RUN pip install -r requirements.txt
ENV FLAG CCTFXOWASP{on3_r3fl3ct1on_n0_m1rr0r}

ENTRYPOINT ["python"]
CMD ["app.py"]