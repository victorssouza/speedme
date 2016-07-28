# Speedme - Network speed analyser


## What is it?

This project is a simple backend-python script that will test your internet using `speed-test` lib

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Pre-requisities

To run this app you will need:
	- Operational System: GNU Linux, MACOS X (with Docker for mac), Windows (with Docker for Windows)

	- Docker version 1.12.0-rc2
	- docker-compose version 1.8.0-rc1


### Installing

A step by step guide to setting up the app and running it

Clone the project wherever you like

```
git clone https://github.com/victorssouza/speedme.git
```

Inside the 'speedme' directory just type the following syntax to run the app for the first time:

```
docker-compose up --build >> log/speedme.log
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

The syntax just runned three containers: a python backend that will post internet metrics into influxdb, an influxdb container to hold the data and finally a grafana container to plot graphs and stuff.

Just type at your browser: `http://localhost` to access grafana's app. Every minute a new metric will be posted and you will be able to see the results from it.

If you want to see the data it self from influxdb container you can access: `http://localhost:8083`

## Tips and tricks

You can play around with docker-compose run with some shell automation if you are using linux, such as:

1) Using the `nohup` command to not hangup the docker-compose process when you leave your shell and running it as a background process
```
nohup docker-compose up --build >> log/speedme.log &
```
or

2) Using the `tee` command to redirect the log output at log/speedme.log and to your shell as well
```
$ docker-compose up --build | tee -a log/speedme.log
```

or

3) Combine an alias with one of your syntaxes to make an easier invoke:
```
alias speedmeup='nohup docker-compose up --build >> log/speedme.log &'
```

### Basic troubleshooting

You can list all current running containers with:

```
docker ps
```

You can stop all running containers with:
```
docker stop $(docker ps -q)
```

You can remove all stopped containers with:
```
docker rm $(docker ps -a -q)
```

You can delete all docker images with:
```
docker rmi $(docker images -q)
```

Have fun! :D

## Documentation

For additional information you can access grafana's and influxdb's docs:

	Grafana: https://github.com/grafana/grafana
	Influxdb: https://github.com/influxdata/influxdb

## Acknowledgments

* Docker usage - basics
* Basic python knowledge (optional)