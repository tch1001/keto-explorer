# Instructions
[Youtube Tutorial](https://youtu.be/OYnHHgYkW2c)

The easiest way to setup a local testing server is to use Docker Compose.

## Using Docker Compose (Recommended)
```
docker compose up -d 
docker ps # check ports are forwarded correctly
curl http://127.0.0.1:4466/health/ready # should be {"status": "ok}
curl http://127.0.0.1:4467/health/ready # should be {"status": "ok}
```
Open `http://127.0.0.1:8888` in your browser
 
# Common Errors
Here are some common errors.

## File Sharing must be enabled
The path keto-explorer/containers/keto is not shared from the host and is not known to Docker.
You can configure shared paths from Docker -> Preferences... -> Resources -> File Sharing.

Solution: Just follow the instructions in the Docker Desktop App.

# Development
```
docker-compose up -d 
ENV_FILE=.env.development FLASK_DEBUG=1 flask run --port 5001 
```
