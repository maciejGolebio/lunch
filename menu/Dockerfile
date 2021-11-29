FROM python:3.10

WORKDIR /usr/src

COPY ./lunch_utils /usr/lunch_utils
COPY ./menu/src/requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 8080

COPY ./menu/src /usr/src

# HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8080/ping || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]