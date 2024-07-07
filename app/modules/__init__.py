from .icmp_daemon import ICMPdaemon
from .nas_daemon import NASdaemon
from .sw_dump import DumperSW
from .forward_gateway import ForwardGatewayServer

dumper_sw = DumperSW()
pinger = ICMPdaemon()
nas_poller = NASdaemon()
vpn_gateway = ForwardGatewayServer()

pinger.start()
nas_poller.start()
vpn_gateway.start()


