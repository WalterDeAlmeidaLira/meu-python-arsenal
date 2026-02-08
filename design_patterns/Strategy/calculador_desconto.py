class CalculadorDescontos:

    def calcula(self, orcamento,desconto_item, desconto_valor):
        desconto = 0
        desconto_item = desconto_item.calcula(orcamento)
        desconto = desconto_item
        if desconto > 0:
            return desconto
        else: 
            desconto = desconto_valor.calcula(orcamento)
        return desconto
        
if __name__ == "__main__":
    from orcamento import Orcamento, Item
    from descontos import DescontoItens, DescontoValor
    desconto_item = DescontoItens()
    desconto_valor = DescontoValor()
    calculado_desconto = CalculadorDescontos()

    orcamento_itens = Orcamento()
    orcamento_itens.adiciona_item(Item("Teclado", 100))
    orcamento_itens.adiciona_item(Item("Mouse", 50))
    orcamento_itens.adiciona_item(Item("Monitor", 400))
    print(orcamento_itens.valor)
    print(orcamento_itens.total_itens)
    print("Desconto Calculado: R$", round(calculado_desconto.calcula(orcamento=orcamento_itens,desconto_item=desconto_item,desconto_valor=desconto_valor),2))

