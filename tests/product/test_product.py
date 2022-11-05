from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=11,
        nome_do_produto="Celular",
        nome_da_empresa="Mi Corporation",
        data_de_fabricacao="2021-02-08",
        data_de_validade="2023-09-05",
        numero_de_serie="CR15 1001 4767 6549 4802 1",
        instrucoes_de_armazenamento="instrucao 15"
    )

    assert product.id == 11
    assert product.nome_do_produto == "Celular"
    assert product.nome_da_empresa == "Mi Corporation"
    assert product.data_de_fabricacao == "2021-02-08"
    assert product.data_de_validade == "2023-09-05"
    assert product.numero_de_serie == "CR15 1001 4767 6549 4802 1"
    assert product.instrucoes_de_armazenamento == "instrucao 15"
