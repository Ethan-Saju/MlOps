IMAGE = ghcr.io/ethan-saju/iris-api:latest
CONTAINER = iris-api

dev:
	docker pull $(IMAGE)
	- docker stop $(CONTAINER) || true
	- docker rm $(CONTAINER) || true
	docker run -d --name $(CONTAINER) -p 8000:8000 $(IMAGE)