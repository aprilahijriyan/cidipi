import logging
import os
import platform
import subprocess
import time
from contextlib import suppress
from typing import Optional
from urllib.parse import quote_plus

from curl_cffi import requests

from cidipi.models import BrowserMetadata, ListTabAdapter, Tab
from cidipi.utils import find_free_port, kill_pid, test_port

logger = logging.getLogger(__name__)

CHROME_PATH_MAPPING = {
    "Windows": [
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        f"{os.getenv('USERPROFILE')}\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
        "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    ],
    "Linux": [
        "google-chrome",
        "google-chrome-stable",
        "google-chrome-beta",
        "google-chrome-dev",
        "microsoft-edge-stable",
    ],
    "Darwin": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ],
}
CHROME_PATHS = CHROME_PATH_MAPPING[platform.system()]


class Browser:
    def __init__(
        self,
        start_url: Optional[str] = "about:blank",
        *,
        chrome_path: Optional[str] = None,
        chrome_args: Optional[list[str]] = None,
        remote_host: Optional[str] = "127.0.0.1",
        remote_port: Optional[int] = 9222,
        headless: Optional[bool] = True,
        user_agent: Optional[str] = None,
        proxy: Optional[str] = None,
    ):
        self.start_url = start_url
        self.chrome_path = (
            chrome_path or os.getenv("CHROME_PATH") or self.find_chrome_path()
        )
        self.chrome_args = chrome_args
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.headless = headless
        self.user_agent = user_agent
        self.proxy = proxy
        self.process: Optional[subprocess.Popen] = None

    def find_chrome_path(self):
        with suppress(KeyError):
            for path in CHROME_PATH_MAPPING[platform.system()]:
                if os.path.exists(path):
                    return path

    def check_port(self):
        if self.remote_port == 0:
            self.remote_port = find_free_port()
            logger.debug(f"Using free port: {self.remote_port}")
        else:
            port_available = test_port(self.remote_port)
            if not port_available:
                raise RuntimeError(
                    f"Unable to use port {self.remote_port}. Port is not available"
                )

    def get_browser_args(self):
        if not self.chrome_path:
            raise RuntimeError("chrome_path is not set. Unable to detect Chrome path")

        if not os.path.isfile(self.chrome_path):
            raise RuntimeError(f"chrome_path is not a file: {self.chrome_path}")

        self.check_port()
        args = [
            self.chrome_path,
            f"--remote-debugging-address={self.remote_host}",
            f"--remote-debugging-port={self.remote_port}",
        ]
        if self.headless:
            args.append("--headless")
            args.append("--hide-scrollbars")
        if self.user_agent:
            args.append(f"--user-agent={self.user_agent}")
        if self.proxy:
            args.append(f"--proxy-server={self.proxy}")
        if self.chrome_args:
            args = args + self.chrome_args
        if self.start_url:
            args.append(self.start_url)
        return args

    @property
    def is_alive(self):
        if not self.process:
            return False
        return self.process.poll() is None

    def start(self):
        if self.is_alive:
            return True

        # kill the old process if it exists
        self.close()
        cmd = subprocess.list2cmdline(self.get_browser_args())
        self.process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return self.chrome_ready()

    def chrome_ready(self, max_retries: int = 10, delay: float = 1.0):
        assert self.is_alive
        next_delay = delay
        for i in range(max_retries):
            attempt = i + 1
            try:
                self.metadata
                logger.debug(f"Chrome ready on {self.remote_host}:{self.remote_port}")
                return True
            except (requests.errors.RequestsError, requests.errors.CurlError):
                logger.debug(
                    f"Chrome not ready on {self.remote_host}:{self.remote_port} (attempt {attempt}/{max_retries})"
                )
                time.sleep(next_delay)

            next_delay = delay * attempt

        return False

    def close(self):
        if self.process:
            logger.debug(
                f"Killing Chrome on {self.remote_host}:{self.remote_port} (PID {self.process.pid})"
            )
            kill_pid(self.process.pid)

    async def __aenter__(self):
        self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def http_uri(self):
        return f"http://{self.remote_host}:{self.remote_port}"

    @property
    def metadata(self):
        url = self.http_uri + "/json/version"
        resp = requests.get(url)
        return BrowserMetadata.model_validate_json(resp.content)

    def get_tabs(self) -> list[Tab]:
        url = self.http_uri + "/json/list"
        resp = requests.get(url)
        tabs = []
        for t in ListTabAdapter.validate_json(resp.content):
            t._browser = self
            tabs.append(t)
        return tabs

    def new_tab(self, url: str = "about:blank", auto_close: bool = True):
        url = self.http_uri + "/json/new?%s" % quote_plus(url)
        resp = requests.put(url)
        tab = Tab.model_validate_json(resp.content)
        tab._browser = self
        tab.set_auto_close(auto_close)
        return tab
