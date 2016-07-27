from jinja2 import Environment, FileSystemLoader, Template
import yaml
import json

ENV = Environment(loader=FileSystemLoader('./'))

with open("./vars/netglobal.yaml") as inputfile:
    netglobal =  yaml.load(inputfile)

with open('./vars/mobile_first/devices.yaml') as inputfile:
    devices = yaml.load(inputfile)

with open('./vars/mobile_first/branch_vars.yaml') as inputfile:
    branch = yaml.load(inputfile)

for device in devices:
    if device['type'] == "5406R":
        template = ENV.get_template("./templates/5406R.j2")
        #print (template.render(netglobals=netglobals, device=device))
        with open("./Configs/"+device['sysname']+"_"+device['manageip']+".cfg", "w") as file:
            file.write(template.render(netglobal=netglobal, device=device, branch=branch))
    if device['type'] == "MSR930":
        template = ENV.get_template("./templates/MSR_CW.j2")
        #print (template.render(netglobals=netglobals, device=device))
        with open("./Configs/"+device['sysname']+"_"+device['manageip']+".cfg", "w") as file:
            file.write(template.render(netglobal=netglobal, device=device, branch=branch))
    if device['type'] == "HPE2920":
        template = ENV.get_template("./templates/2920stack.j2")
        # print (template.render(netglobals=netglobals, device=device))
        with open("./Configs/" + device['sysname'] + "_" + device['manageip'] + ".cfg", "w") as file:
            file.write(template.render(netglobal=netglobal, device=device, branch=branch))



# Print dictionary generated from yaml


# Render template and print generated config to console
#template = ENV.get_template("Comware5_Template.j2")
#print (template.render(network_global=network_global, device_values = device_values, site= site))

