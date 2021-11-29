SHELL := /bin/bash -o pipefail -o errexit

MENU_IMAGE=lunch/menu
ORDERS_IMAGE=lunch/orders

run-k3s:
	sudo k3s server --docker &

stop-k3s:
	sudo systemctl stop k3s

build-menu-image:
	docker build -t $(MENU_IMAGE) -f menu/Dockerfile .

build-orders-image:
	docker build -t $(ORDERS_IMAGE) -f orders/Dockerfile .

deploy-menu:
	sudo k3s kubectl apply -f menu/api.yml; \
	sudo k3s kubectl port-forward service/menu-api-svc 8080;

delete-menu:
	sudo k3s kubectl delete -f menu/api.yml;

deploy-orders:
	sudo k3s kubectl apply -f orders/mongo-secrets.yml; \
	sudo k3s kubectl apply -f orders/mongo.yml; \
	sudo k3s kubectl apply -f orders/mongo-configmap.yml; \
	sudo k3s kubectl apply -f orders/mongo-express.yml; \
	sudo k3s kubectl apply -f orders/api.yml;

delete-orders:
		sudo k3s kubectl delete -f orders/mongo-secrets.yml; \
        sudo k3s kubectl delete -f orders/mongo.yml; \
        sudo k3s kubectl delete -f orders/mongo-configmap.yml; \
        sudo k3s kubectl delete -f orders/mongo-express.yml; \
        sudo k3s kubectl delete -f orders/api.yml;

