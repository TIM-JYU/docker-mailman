# Local GNU Mailman 3 Deployment with Docker

This repository hosts code for two docker images `timimages/mailman-core` and
`timimages/mailman-web` both of which are meant to deploy GNU Mailman 3 in
a local development and testing environment.

The code is based on [maxking/docker-mailman](https://github.com/maxking/docker-mailman) but is modified to

* better work with SQLite database and logs mapped to a Docker host's folder;
* include helper scripts to set up mailman for testing and send test mail.

Refer to the original repository for documentation on available environment variables.

## Building

To build the image, use 

```
./build.sh [<docker.io registry>] [<version tag>]
```

where both arguments are optional.
