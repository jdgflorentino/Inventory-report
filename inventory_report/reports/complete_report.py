from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    def get_total_products(product_list):
        return Counter(
            product["nome_da_empresa"]
            for product in product_list).most_common()

    @classmethod
    def generate(self, product_list):
        total_products = self.get_total_products(product_list)
        result = ""
        for company, qty in total_products:
            result += f"- {company}: {qty}\n"
        simple_report = super().generate(product_list)

        return (
          f"{simple_report}\n"
          + "Produtos estocados por empresa:\n"
          + result)
