"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""
import json
import xml.etree.ElementTree as ET

def calcular_faturamento(arquivo, formato):

    if formato == 'json':
        with open(arquivo, 'r') as f:
            dados = json.load(f)
    elif formato == 'xml':
        tree = ET.parse(arquivo)
        root = tree.getroot()
        dados = [float(dia.text) for dia in root.findall('dia')]
    else:
        raise ValueError("Formato de arquivo inválido.")

    faturamentos = [valor for valor in dados if valor > 0]
    
    media = sum(faturamentos) / len(faturamentos)
    menor = min(faturamentos)
    maior = max(faturamentos)

    dias_acima_media = sum(valor > media for valor in faturamentos)

    return menor, maior, dias_acima_media

arquivo = './questao3/questao3.json'
formato = 'json'

menor, maior, dias_acima_media = calcular_faturamento(arquivo, formato)

print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
