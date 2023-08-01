#!/usr/bin/make

SHELL = /bin/bash

UID := $(shell id -u)
GID := $(shell id -g)

export UID
export GID

shell:
	docker-compose -f docker-compose.yml exec -u ${UID}:${GID} py-script-service bash

up:
	docker-compose -f docker-compose.yml up --build -d

down:
	docker-compose -f docker-compose.yml down

log:
	docker logs --follow py-script