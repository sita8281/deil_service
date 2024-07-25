from threading import Thread
import time


class SessionMaker(Thread):
    _online_users = []

    def run(self) -> None:
        while True:
            time.sleep(10)
