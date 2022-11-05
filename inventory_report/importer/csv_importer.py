import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(data)
