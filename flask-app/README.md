## Deploy with Dockerfile

```
$ docker build . -t flask-app
$ docker run -dit -p 80:5000 flask_app
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE       COMMAND            CREATED         STATUS         PORTS                  NAMES
a302c2e69793   flask-app   "python3 app.py"   5 seconds ago   Up 3 seconds   0.0.0.0:80->5000/tcp   exciting_antonelli
```

After the application starts, navigate to `http://localhost:80` in your web browser or run:
```
$ curl localhost:80
Hello World! We have Flask in a Docker container!
```

Stop and remove the containers
```
$ docker stop a302c2e69793
$ docker rm a302c2e69793
```