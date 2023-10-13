ARG BUILD_FROM
FROM $BUILD_FROM
RUN apk add --update --no-cache py3-opencv py3-requests
COPY ha_cam_tag /opt/ha_cam_tag
WORKDIR /opt
ENTRYPOINT [ "/usr/bin/python3", "-mha_cam_tag" ]
