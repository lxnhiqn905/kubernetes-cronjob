COMMANDS

    docker build . -t count-date-app

    kubectl create -f count-date-data-runtime-volume-conf.yaml

    kubectl create -f count-date-job-conf.yaml

    kubectl get pods

    kubectl logs <pod-id>

EXPLAINED

    1. Create the docker image that include your application

    2. Create the kubernetes CronJob with the docker image that created at Step-1

    3. At schedule time, kubernetes will be create Container to execute your application and shutdown the container after complete.

    4. The data-file use to store data runtime will be saved at vitual volume that manage by kubernetes