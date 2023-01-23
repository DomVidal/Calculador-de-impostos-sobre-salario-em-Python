import time
#informação sobre o usuario
horas1 = float(int(input("Quanto você ganha por hora?")))
horas_trabalhadas = float(int(input("Quantas horas você trabalha por mês?")))

#resultado das informações
resultado = (horas1 * horas_trabalhadas)
print("Seu salário bruto é de:", resultado)

#tempo para não ficar embolado
time.sleep(2)

#resultado imposto IR
resultado_ir = resultado - (resultado*11/100)
print("Seu salário bruto, - IR, fica", resultado_ir)

#tempo para não ficar embolado
time.sleep(3)

#resultado imposto INSS
resultado_inss = resultado_ir - (resultado_ir*8/100)
print("Seu salário bruto, - IR, - INSS fica", resultado_inss)

#tempo para não ficar embolado
time.sleep(4)

#resultado imposto sindicato
resultado_sind = resultado_inss - (resultado_inss*5/100)
print("Seu salário bruto, - IR, - INSS, - Sindicato, fica", resultado_sind)

#tempo para não ficar embolado
time.sleep(5)

#salario liquido
print("Seu salário líquido é de:", resultado_sind)