# Fork of Computer Vision Annotation Tool (CVAT)

This is my fork of the [CVAT](https://github.com/opencv/cvat/tree/develop) which has been modified to support our system's user directory structure, LDAP authentication, and requirements for loading NITF files.

Command to start docker containers:
```sudo docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d --build```
