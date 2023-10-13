import logging
import re
import signal
import sys
import threading
import time
import json
import os
import requests
from datetime import datetime, timedelta

import cv2

CONFIG_PATH = "/data/options.json"
API_URL = "http://supervisor/core/api/"
AUTH_TOKEN = os.environ['SUPERVISOR_TOKEN']
DEBOUNCE_PERIOD = timedelta(seconds=5)
TAG_ID_PATTERN = re.compile('https://www.home-assistant.io/tag/([0-9a-fA-F-]+)')

def send_tag_event(tag_id, device_id):
    endpoint = f"{API_URL}events/tag_scanned"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    data = {
        "tag_id": tag_id,
        "device_id": device_id
    }
    requests.post(endpoint, headers=headers, json=data)

def main():
    with open(CONFIG_PATH, 'r') as fh:
        config = json.load(fh)

    exiting = False
    frame = None
    cv = threading.Event()

    def detector_loop():
        detector = cv2.QRCodeDetector()
        last_time, last_tag = None, None
        while not exiting:
            cv.wait()
            try:
                if not exiting and (data := detector.detectAndDecode(frame)[0]) and (m := TAG_ID_PATTERN.match(data)):
                    cur_time, tag_id = datetime.now(), m.group(1)
                    if last_tag != tag_id or last_time < cur_time - DEBOUNCE_PERIOD:
                        send_tag_event(tag_id, config['tag_event_device_id'])
                        last_time, last_tag = cur_time, tag_id
            except Exception as e:
                logging.exception(e)

    detector_thread = threading.Thread(target=detector_loop)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    detector_thread.start()
    signal.signal(signal.SIGINT, signal.default_int_handler)

    try:
        while True:
            stream = cv2.VideoCapture(config['camera_rtsp_stream'])
            while stream.isOpened():
                if (frame := stream.read()[1]) is not None:
                    cv.set()
            stream.release()
            time.sleep(5)
    except KeyboardInterrupt:
        exiting = True
        cv.set()

    detector_thread.join()
    return 0

if __name__ == "__main__":
    main()
