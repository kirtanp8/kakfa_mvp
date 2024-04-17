# kakfa_mvp

minikube start
docker build -t flask-kafka .
docker push <your-docker-username>/flask-kafka:latest
kubectl apply -f kubernetes.yaml
minikube service flask-kafka
curl -X POST -H "Content-Type: application/json" -d '{"message":"Hello Kafka"}' http://<minikube-service-ip>/produce
curl http://<minikube-service-ip>/consume
