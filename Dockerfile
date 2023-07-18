FROM python:3

WORKDIR /usr/src/app

COPY jobs/* ./

CMD [ "python", "count-date.py" ]
