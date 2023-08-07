# FastAPI + Celery
A basic boilerplate to serve an API rest using `FastAPI` and a `Celery` worker to receive and execute async tasks.

# Installation
You need to have `Poetry` and `Make` installed, then execute:
```
# Activate a virtual env
make shell

# Install dependencies
make install
```

# Run the application
You can start the API server and Celery worker locally using the following commands:  

```
# Start FastAPI server
make run
```

Once the server is running, start the Celery worker:
```
# Open another terminal and execute
poetry run celery -A src.api.main.celery worker --loglevel=info
```

Optionally you can start the `Flower` server to track the celery tasks in "real-time":
```
# In another terminal execute
poetry run celery -A src.api.main.celery flower --port=5555
```

Then you can go to http://localhost:5555 to see the Flower UI application.

## Using docker compose
Also is possible to start the whole stack using `docker compose`
To do so, execute the following command:
```
# On the main folder containing the file `docker-compose.yml`
docker compose up -d
```
## Using the application
Once the application is up, the API server is ready to receive task requests.
Go to http://localhost:8000/docs to see all available endpoints to tryout. 
