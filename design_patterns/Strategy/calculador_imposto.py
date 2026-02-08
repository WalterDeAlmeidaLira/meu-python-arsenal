class CalculadorImpostos:

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento=orcamento)
        return imposto_calculado


