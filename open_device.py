import os
import napalm
import datetime
from napalm import get_network_driver

path = os.getcwd()  # assign current working directory of a process.
try:
    os.stat(path + "/backup_config")   # performs a stat system call on the given path.
except:
    os.mkdir(path + "/backup_config")  # create backup_config directory for backup files

driver = get_network_driver("ios")  # 
device_list = ["192.168.43.100", "10.1.1.1", "10.1.1.2", "10.1.1.3"] 
user = "admin"
passw = "cisco123"
optional_args = {"secret": "cisco"}

for ip in device_list:
    device = driver(
        hostname=ip, username=user, password=passw, optional_args=optional_args
    )
    device.open()
    config = device.get_config(retrieve="running")
    facts = device.get_facts()
    run_config = config["running"]
    hostname = facts["hostname"]
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    file = open(path + "/backup_config/" + hostname + "_" + date + "_" + "running-config", "w")
    file.write(run_config)
    file.close()
    device.close()
    print('Done')
