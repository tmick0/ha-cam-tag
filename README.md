# ha-cam-tag

This is a simple program to detect QR codes containing Home Assistant tags in an RTSP stream and send `tag_scanned` events to Home Assistant.

Fill in the config file with the following information:
- `uri`: URI of the Home Assistant API, e.g. http://homeassistant.local:8123/api/
- `auth-token`: A long-lived access token for Home Assistant
- `device-id`: Device ID to set for the origin of the events, e.g. the ID of the camera device
- `stream`: URI of the RTSP stream to consume

For more details on setting up the Home Assistant API, see https://developers.home-assistant.io/docs/api/rest/

More info on this project at https://lo.calho.st/posts/homeassistant-qr-code-detection/
