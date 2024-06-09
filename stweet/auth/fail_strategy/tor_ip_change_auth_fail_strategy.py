import time

try:
    from tor_python_easy.tor_control_port_client import TorControlPortClient
except ImportError:
    raise ImportError("Tor related imports are not available. Please install the [tor] extra")

from stweet.auth.fail_strategy.auth_fail_strategy import AuthFailStrategy


class TorIpChangeAuthFailStrategy(AuthFailStrategy):
    tor_control_port_client: TorControlPortClient

    def __init__(self, tor_control_port_client: TorControlPortClient):
        self.tor_control_port_client = tor_control_port_client

    def run_strategy(self) -> None:
        time.sleep(5)
        self.tor_control_port_client.change_connection_ip()
