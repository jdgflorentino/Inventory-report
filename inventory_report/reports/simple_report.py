from datetime import datetime
from collections import Counter


class SimpleReport:

    def get_oldest_data(product_list):
        return (min(
            [product["data_de_fabricacao"] for product in product_list]))

    def get_closest_data(product_list):
        return min([
                    product["data_de_validade"]
                    for product in product_list
                    if product["data_de_validade"] > str(datetime.now())
        ])

    def get_company(product_list):
        return Counter(
            [product["nome_da_empresa"] for product in product_list]
        ).most_common()[0][0]

    @staticmethod
    def generate(product_list):

        oldest_date = SimpleReport.get_oldest_data(product_list)
        closest_date = SimpleReport.get_closest_data(product_list)
        company = SimpleReport.get_company(product_list)
        expected = (
          f"Data de fabricação mais antiga: {oldest_date}\n"
          f"Data de validade mais próxima: {closest_date}\n"
          f"Empresa com mais produtos: {company}")
        return expected
