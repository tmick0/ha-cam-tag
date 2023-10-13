# Streaming Camera Tag Detection for Home Assistant

This is a simple Home Assistant add-on to detect QR codes containing tag URLs in an RTSP stream and generate `tag_scanned` events from them.

More info on this project at https://lo.calho.st/posts/homeassistant-qr-code-detection/

## Installation

### Step 1: Add repository

You can add this repository to your Home Assistant instance by clicking this link:

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftmick0%2Fha-cam-tag)

If for whatever reason that doesn't work, follow these steps:

1. Go to `Settings -> Add-ons -> Add-on Store` in your Home Assistant instance
2. From the three-dots menu in the top right, select `Repositories`
3. Enter the URI of this repository `https://github.com/tmick0/ha-cam-tag` and click Add

### Step 2: Install add-on

After adding the repository, refresh the Add-on Store. Then, you should be able to choose the `Streaming Camera Tag Detection` add-on and install it.

### Step 3: Configuration

After installation, set up the following configuration for the add-on:

- `tag_event_device_id`: Device ID to set for the origin of the events, e.g. the ID of the camera device
- `camera_rtsp_stream`: URI of the RTSP stream to consume

Finally, start the plugin. It is recommended to enable the watchdog in case anything fails.

