## Deploy with docker compose

```
$ docker compose up -d
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                  NAMES
2bc8271fee81        php-docker_web               "docker-php-entrypoi…"   About a minute ago  Up About a minute   0.0.0.0:80->80/tc    php-docker_web_1
```

After the application starts, navigate to `http://localhost:80` in your web browser or run:
```
$ curl localhost:80
Hello World! We have Apache-PHP in a Docker container using docker compose!
```

Stop and remove the containers
```
$ docker compose down
```