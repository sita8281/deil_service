from threading import Thread
import time
import uuid


class SessionMaker(Thread):
    _online_users = {}
    daemon = True

    def run(self) -> None:
        print(' * Web Sessions Daemon: on')
        while True:
            time.sleep(1)
            try:
                for key, val in self._online_users.items():
                    if time.time() - val[1] > 10:
                        self._disconnect(key)
            except Exception:
                pass

    def connect(self, session_token: str, remote_ip: str) -> None:
        self._online_users[session_token] = [remote_ip, int(time.time()), 'connect', str(uuid.uuid4())]

    def _disconnect(self, session_token: str) -> None:
        if session_token in self._online_users:
            del self._online_users[session_token]

    def logout_signal(self, session_token) -> None:
        if session_token in self._online_users:
            self._online_users[session_token][2] = 'logout'

    @property
    def get_connections(self) -> dict:
        return self._online_users



