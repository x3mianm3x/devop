import json
import netmiko
from netmiko import ConnectHandler

# Parse the Data from Json file to Python Variable
with open('configcisco1.json') as config_file:
    config = json.load(config_file)
    
# Extract the configuration date:
device_info = config['device']
interface_config = config['interface_config']
new_hostname = config['new_hostname']

# Connect to Cisco via SSH:
net_connect = ConnectHandler(**device_info)

# Enter enable mode
net_connect.enable()

#Build the Configuration:
commands =[
    f"interface {interface_config['interface']}",
    f"ip address {interface_config['new_ip']} {interface_config['subnet_mask']}",
    "no shutdown", #make sure its up
    "exit",
    f"hostname {new_hostname}"
]

# Send the json parsed python file to Cisco
output = net_connect.send_config_set(commands)
print(output)

# always close the connection:
net_connect.disconnect