FROM python:3-alpine

# Change this key
ENV secretKey d1c06464c4

#RUN apk --no-cache add python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src /app

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "login.py" ]
