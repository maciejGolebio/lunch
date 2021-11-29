FROM python:3.10

WORKDIR /usr/src

COPY ./lunch_utils /usr/lunch_utils
COPY ./orders/src/requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 80

COPY ./orders/src /usr/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]