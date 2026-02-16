class CalculadorDescontos:

    def calcula(self, orcamento,desconto):
        desconto_do_orcamento = desconto.calcula(orcamento=orcamento)
        return desconto_do_orcamento
        
        
if __name__ == "__main__":
    from orcamento import Orcamento, Item
    from descontos import DescontoItens, DescontoValor, SemDesconto
    
    desconto_item = DescontoItens(proximo_desconto=DescontoValor(proximo_desconto=SemDesconto()))
    calculado_desconto = CalculadorDescontos()

    orcamento_itens = Orcamento()
    orcamento_itens.adiciona_item(Item("Teclado", 100))
    orcamento_itens.adiciona_item(Item("Mouse", 50))
    orcamento_itens.adiciona_item(Item("Monitor", 400))
    print("Valor de Orçamento: R$",orcamento_itens.valor)
    print("Total de itens no orçamento:",orcamento_itens.total_itens)
    desconto_calculado = round(calculado_desconto.calcula(orcamento=orcamento_itens,desconto=desconto_item),2)
    print("Desconto Calculado: R$",desconto_calculado)

