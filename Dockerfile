FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipeline.py .
COPY generate_sensors_data.sh .

ENTRYPOINT [ "python", "pipeline.py" ] 