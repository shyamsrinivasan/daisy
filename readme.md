## An application for farm operation resource planning
- Running Docker requires WSL2 with Ubuntu 22.04


### Running Redis on Docker
- `docker run -d redis --name redis-server -p 6379:6379 bind 0.0.0.0` runs the docker image `redis` with name `redis-server` and binds the docker port `6379` to port `6379` on the IP address `0.0.0.0` mentioned after `bind`
- stop docker service using `docker stop redis-server` where the name of the service to be stopped is the name provided for `--name` when starting the docker service
- since docker is run locally on the machine the redis host in python should be either `localhost` or `127.0.0.1` and the port should be `6379`

