from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory():
    def open_files(path):
        if path.endswith(".csv"):
            with open(path) as file:
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))

        if path.endswith(".json"):
            with open(path) as file:
                return list(json.load(file))

        if path.endswith(".xml"):
            with open(path) as file:
                xml = xmltodict.parse(file.read())
                return xml["dataset"]["record"]

    @staticmethod
    def import_data(path, type):
        data = Inventory.open_files(path)

        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
