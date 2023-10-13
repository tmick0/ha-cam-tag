# Streaming Camera Tag Detection for Home Assistant

This is a simple Home Assistant add-on to detect QR codes containing tag URLs in an RTSP stream and generate `tag_scanned` events from them.

Since this is not an official add-on, you must follow these steps to install it:

1. Go to `Settings -> Add-ons -> Add-on Store` in your Home Assistant instance
2. From the three-dots menu in the top right, select `Repositories`
3. Enter the URI of this repository `https://github.com/tmick0/ha-cam-tag.git` and click Add

After installation, set up the following configuration for the add-on:

- `tag_event_device_id`: Device ID to set for the origin of the events, e.g. the ID of the camera device
- `camera_rtsp_stream`: URI of the RTSP stream to consume

Then, you can start it up.

More info on this project at https://lo.calho.st/posts/homeassistant-qr-code-detection/
