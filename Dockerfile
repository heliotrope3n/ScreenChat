FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install flask

# Bundle app source
COPY hello.py /src/hello.py
COPY . /templates
COPY . /static

CMD ["python", "/src/hello.py"]
