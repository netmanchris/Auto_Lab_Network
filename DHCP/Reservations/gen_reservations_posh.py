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





