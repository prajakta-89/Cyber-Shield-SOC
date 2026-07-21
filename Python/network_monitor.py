from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from network_detector import detect_network_threat

import time

LOG_FILE = "network_traffic.log"

last_position = 0


class LogHandler(FileSystemEventHandler):

    def on_modified(self, event):

        global last_position

        if not event.src_path.endswith(LOG_FILE):
            return

        with open(LOG_FILE, "r") as file:

            file.seek(last_position)

            new_lines = file.readlines()

            last_position = file.tell()

        for line in new_lines:

            detect_network_threat(line)


observer = Observer()

observer.schedule(LogHandler(), ".", recursive=False)

observer.start()

print("🌐 Network Monitor Started")

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()