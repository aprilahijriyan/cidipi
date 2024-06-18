import asyncio
import socket
from typing import Optional

import psutil


class AtomicInteger:
    def __init__(self, initval=0):
        self.val = initval
        self.lock = asyncio.Lock()

    async def increment(self):
        async with self.lock:
            self.val += 1
        return self.val

    async def decrement(self):
        async with self.lock:
            self.val -= 1
        return self.val


def kill_pid(pid: int):
    proc = psutil.Process(pid)
    try:
        proc.kill()
        try:
            return proc.wait(0.1)
        except psutil.TimeoutExpired:
            pass
    except (psutil.NoSuchProcess, ProcessLookupError):
        pass


def test_port(port: int, timeout: Optional[float] = 1) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.bind(("", port))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def find_free_port(port=1024, max_port=65535):
    while port <= max_port:
        available = test_port(port)
        if available:
            return port
        port += 1
    return None
