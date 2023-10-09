# Instructions
[Youtube Tutorial](TODO)

There are many ways to setup a local copy, but the easiest is to use Docker Compose.

## Using Docker Compose (Recommended)
```

```

# Common Errors
Here are some common errors.

## File Sharing must be enabled
The path keto-explorer/containers/keto is not shared from the host and is not known to Docker.
You can configure shared paths from Docker -> Preferences... -> Resources -> File Sharing.

Solution: Just follow the instructions in the Docker Desktop App.

# Development
```
docker-compose up -d 
docker ps # make sure ports are forwarded
ENV_FILE=.env.development && flask run --port 5001
```
