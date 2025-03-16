## An application for farm operation resource planning
- Running Docker requires WSL2 with Ubuntu 22.04


### Running Redis on Docker
- `docker run -d redis --name redis-server -p 6379:6379 bind 0.0.0.0` runs the docker image `redis` with name `redis-server` and binds the docker port `6379` to port `6379` on the IP address `0.0.0.0` mentioned after `bind`
- stop docker service using `docker stop redis-server` where the name of the service to be stopped is the name provided for `--name` when starting the docker service
- since docker is run locally on the machine the redis host in python should be either `localhost` or `127.0.0.1` and the port should be `6379`

### Run FastAPI in WSL2 and access it from Windows:
- start wsl2 using `wsl` or `wsl -d <Distro>`
- go to the relevant directory where your FastAPI application is stored (in Windows)
- Update python (if needed) and create a new virtual environment for linux using `python3 -m venv env-linux` so as to not to confuse with the virtual environment created for windows
- activate the virtual environment using `source env-linux/bin/activate`
- install dependencies using `pip install -r requirements`
- check the ip address on which WSL2 is running using `ip addr show eth0 | grep 'inet' | awk '{print $2}' | cut -d/ -f1`
- start the FastAPI application: `uvicorn app:app --host 0.0.0.0 --port 8000`
- access the app from windows using the WSL ip address and port given when starting the FastAPI application

