'''Copyright 2015 Christopher Young ( @netmanchris )

Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
Unless required'''

from jinja2 import Environment, FileSystemLoader, Template
import yaml
import csv
import json

ENV = Environment(loader=FileSystemLoader('./'))
template = ENV.get_template("add_client_reservations_ps.j2")
with open('Reservations.csv') as csvfile:
    content = csv.DictReader(csvfile)
    reservations = []
    for row in content:
        reservations.append(row)
with open("./final_reservations.ps1", "w") as file:
    file.write(template.render(reservations=reservations))





