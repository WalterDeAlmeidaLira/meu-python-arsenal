from orcamento import Orcamento
from imposto import ISS, ICMS
from calculador_imposto import CalculadorImpostos

def main(valor: float):
    orcamento = Orcamento(valor)
    iss = ISS()
    icms = ICMS()
    calculador = CalculadorImpostos()
    print(f"Calculando impostos para um orçamento no valor de R${orcamento.valor}\n## Aguarde...")
    imposto_calculado_iss = calculador.realiza_calculo(orcamento, iss)
    print(f"Imposto calculado ISS: {imposto_calculado_iss}")

    imposto_calculado_icms = calculador.realiza_calculo(orcamento, icms)
    print(f"Imposto calculado ICMS: {imposto_calculado_icms}")

if __name__ == "__main__":
    main(valor=100.0)