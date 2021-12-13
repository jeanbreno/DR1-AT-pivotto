import matplotlib.pyplot as plt

def calculadora_juros_compostos(deposito_inicial, taxa_de_juros, aporte_mensal, periodo):
  saldo = deposito_inicial

  saldo_mensal = []
  print(f"\n\tResultado do investimento após {periodo} mês(es) é: \n")
  for i in range(periodo):
      saldo = saldo + (saldo * (taxa_de_juros / 100)) + aporte_mensal
      saldo_mensal.append(saldo)
      print (f"\t → Saldo do mês {i+1} é de R$ {saldo:,.2f}.")
  total_juros_acumulados = saldo - deposito_inicial - (periodo * aporte_mensal)
  print (f"\nO ganho obtido com os juros foi de R$ {total_juros_acumulados:,.2f}.\n\n")
  plt.plot(saldo_mensal)
  plt.ylabel('Evolução do Patrimônio')
  plt.xlabel('Tempo')
  plt.show()
 # print(saldo_mensal)

deposito_inicial = float(input("Depósito inicial: "))
taxa_de_juros = float(input("Taxa de juros (%): "))
aporte_mensal = float(input("Depósito mensal:"))
periodo = int(input("Periodo: "))

calculadora_juros_compostos(deposito_inicial, taxa_de_juros, aporte_mensal, periodo)
