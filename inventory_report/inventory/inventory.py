from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory():
    def open_files(path):
        if path.endswith(".csv"):
            with open(path) as file:
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))

    @staticmethod
    def import_data(path, type):
        data = Inventory.open_files(path)

        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
