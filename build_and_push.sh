docker login -u $DOCKER_USER -p $DOCKER_PASS

# tensorflow:2.0.0a0-py36-cpu.3
docker build -t $DOCKER_REPO/tensorflow:2.0.0a0-py36-cpu.3 -f openbayes-docker/Dockerfile.tensorflow-2.0.0a0-py36-cpu .
docker push $DOCKER_REPO/tensorflow:2.0.0a0-py36-cpu.3

# tensorflow:2.0.0a0-py36-cu100.3
docker build -t $DOCKER_REPO/tensorflow:2.0.0a0-py36-cu100.3 -f openbayes-docker/Dockerfile.tensorflow-2.0.0a0-py36-cu100 .
docker push $DOCKER_REPO/tensorflow:2.0.0a0-py36-cu100.3

# tensorflow:1.13.1-py36-cpu.3
docker build -t $DOCKER_REPO/tensorflow:1.13.1-py36-cpu.3 -f openbayes-docker/Dockerfile.tensorflow-1.13.1-py36-cpu .
docker push $DOCKER_REPO/tensorflow:1.13.1-py36-cpu.3

# tensorflow:1.13.1-py36-cu100.3
docker build -t $DOCKER_REPO/tensorflow:1.13.1-py36-cu100.3 -f openbayes-docker/Dockerfile.tensorflow-1.13.1-py36-cu100 .
docker push $DOCKER_REPO/tensorflow:1.13.1-py36-cu100.3
