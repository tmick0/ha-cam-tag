import argparse
import logging
import re
import signal
import sys
import threading
import time
from datetime import datetime, timedelta

import cv2
import homeassistant_api as ha
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

DEBOUNCE_PERIOD = timedelta(seconds=5)
TAG_ID_PATTERN = re.compile('https://www.home-assistant.io/tag/([0-9a-f-]+)')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config')
    args = parser.parse_args()

    with open(args.config, 'r') as fh:
        config = yaml.load(fh, Loader=Loader)['ha-cam-tag']
    
    exiting = False
    frame = None
    cv = threading.Event()

    def detector_loop():
        detector = cv2.QRCodeDetector()
        last_time, last_tag = None, None
        with ha.Client(config['homeassistant']['uri'], config['homeassistant']['auth-token']) as client:
            while not exiting:
                cv.wait()
                try:
                    if not exiting and (data := detector.detectAndDecode(frame)[0]) and (m := TAG_ID_PATTERN.match(data)):
                        cur_time, tag_id = datetime.now(), m.group(1)
                        if last_tag != tag_id or last_time < cur_time - DEBOUNCE_PERIOD:
                            client.fire_event("tag_scanned", tag_id=tag_id, device_id=config['camera']['device-id'])
                            last_time, last_tag = cur_time, tag_id
                except Exception as e:
                    logging.exception(e)

    detector_thread = threading.Thread(target=detector_loop)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    detector_thread.start()
    signal.signal(signal.SIGINT, signal.default_int_handler)

    try:
        while True:
            stream = cv2.VideoCapture(config['camera']['stream'])
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
