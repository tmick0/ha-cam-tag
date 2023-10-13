# Streaming Camera Tag Detection for Home Assistant

This is a simple Home Assistant add-on to detect QR codes containing tag URLs in an RTSP stream and generate `tag_scanned` events from them.

After installation, set up the following configuration for the add-on:

- `tag_event_device_id`: Device ID to set for the origin of the events, e.g. the ID of the camera device
- `camera_rtsp_stream`: URI of the RTSP stream to consume

Then, you can start it up.

More info on this project at https://lo.calho.st/posts/homeassistant-qr-code-detection/
