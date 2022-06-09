# Containerized Data Pipeline

## How it works
- Wrote a bash script to generate daily random sensors data [`generate_sensors_data.sh`](/generate_sensors_data.sh)
- Developed a simple ETL pipeline [`pipeline.py`](/pipeline.py)
- Put the pipeline into a Docker container [`Dockerfile`](/Dockerfile)
- Run PostgreSQL and pgAdmin containers to ingest and view data [`docker-compose.yml`](/docker-compose.yml)


## How to run
- To run the pipeline, you will need:
  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - [Docker](https://docs.docker.com/get-docker/)
  - [Docker Compose](https://docs.docker.com/compose/install/)

- Clone the git repo and run the pipeline as shown below:
```bash
git clone https://github.com/sharkawy98/containerized-pipeline
cd containerized-pipeline

# PostgreSQL & pgAdmin
docker compose up -d

# pipeline.py
docker build -t <container-name>
docker run -it --netowrk=<docker-compose-network> <container-name>
```

## Final result
![image](https://user-images.githubusercontent.com/36075516/172742856-3578d7bf-cb91-4ea5-9a1c-b279e0105128.png)
