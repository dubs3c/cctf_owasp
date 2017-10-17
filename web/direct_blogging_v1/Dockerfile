FROM frolvlad/alpine-python3
COPY . /app
WORKDIR /app
RUN pip3 install flask gunicorn
ENTRYPOINT ["/usr/bin/gunicorn", "--config", "gunicorn.py"]
CMD ["go:app"]
