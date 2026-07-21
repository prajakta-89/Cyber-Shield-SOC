from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from detector import detect_threat
import time

LOG_FILE = "server_access.log"

last_position = 0


class LogHandler(FileSystemEventHandler):

    def on_modified(self, event):

        global last_position

        if event.src_path.endswith(LOG_FILE):

            with open(LOG_FILE, "r") as file:

                file.seek(last_position)

                new_lines = file.readlines()

                last_position = file.tell()

            for line in new_lines:

                detect_threat(line)


observer = Observer()

handler = LogHandler()

observer.schedule(handler, ".", recursive=False)

observer.start()

print("🛡 CyberShield Monitor Started")

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()