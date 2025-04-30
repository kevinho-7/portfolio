import csv
import os
from datetime import datetime

def get_senha():
    password = "!Noceutempao1043"
    return password


def get_funcionario():
    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, "funcionarios_santanna.csv")

    cpfs = []
    with open(csv_path, newline='', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for _, cpf in reader:
            cpfs.append(cpf)

    return cpfs
               
def convert_string_to_dates(data):
    return [datetime.strptime(s, "%d/%m/%Y").date() for s in data]
