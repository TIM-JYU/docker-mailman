#!/bin/sh

registry="$1"
version_tag="$2"

docker build -t mailman-core:latest core/
docker build -t mailman-web:latest web/

if [ -n "$registry" ]; then
    docker tag mailman-core "$registry/mailman-core:latest"
    docker tag mailman-web "$registry/mailman-web:latest"
    
    docker push "$registry/mailman-core:latest"
    docker push "$registry/mailman-web:latest"

    if [ -n "$version_tag" ]; then
        docker tag mailman-core "$registry/mailman-core:$version_tag"
        docker tag mailman-web "$registry/mailman-web:$version_tag"

        docker push "$registry/mailman-core:$version_tag"
        docker push "$registry/mailman-web:$version_tag"
    fi
fi