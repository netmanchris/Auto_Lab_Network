from jinja2 import Environment, FileSystemLoader, Template
import yaml
import json

ENV = Environment(loader=FileSystemLoader('./'))

with open("dhcp_scopes.yml") as inputfile:
    dhcpscopes =  yaml.load(inputfile)


template = ENV.get_template("add_dhcp_ps.j2")
#print (template.render(devglobals=devglobals, dev=dev))
with open("./final_dhcp.ps1", "w") as file:
    file.write(template.render(dhcpscopes=dhcpscopes))

# Print dictionary generated from yaml


# Render template and print generated config to console
#template = ENV.get_template("Comware5_Template.j2")
#print (template.render(network_global=network_global, device_values = device_values, site= site))

