import napalm
from napalm import get_network_driver

get_network_driver('ios')
device=driver(hostname="127.0.0.1",
username="admin", password="cisco123", optional_args={"secret": 'cisco'})

device.open()

device.close()

print('Done')
