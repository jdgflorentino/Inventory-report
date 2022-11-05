from inventory_report.inventory.product import Product

mock = "O produto Celular fabricado em 2021-02-08 por Mi Corporation \
com validade até 2023-09-05 precisa ser armazenado instrucao 15."


def test_relatorio_produto():
    product = Product(
        id=11,
        nome_do_produto="Celular",
        nome_da_empresa="Mi Corporation",
        data_de_fabricacao="2021-02-08",
        data_de_validade="2023-09-05",
        numero_de_serie="CR15 1001 4767 6549 4802 1",
        instrucoes_de_armazenamento="instrucao 15"
    )

    report = str(product)
    assert report == mock
