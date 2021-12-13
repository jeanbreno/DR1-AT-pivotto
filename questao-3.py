def diagnosticar_percentual_comprometido(renda_total_mensal, gastos_moradia, gastos_educacao, gastos_transporte):
  valor_ideal_moradia = round((renda_total_mensal * 0.3), 2)
  valor_ideal_educacao = round((renda_total_mensal * 0.2), 2)
  valor_ideal_transporte = round((renda_total_mensal * 0.15), 2)

  percentual_real_gastos_moradia = round(((gastos_moradia / renda_total_mensal) * 100), 2) 

  percentual_real_gastos_educacao = round(((gastos_educacao / renda_total_mensal) * 100), 2)

  percentual_real_gastos_transporte = round(((gastos_transporte / renda_total_mensal) * 100), 2)

  if gastos_moradia > valor_ideal_moradia:
    moradia = f"O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {valor_ideal_moradia}."
  else:
    moradia = f"O máximo recomendado é de 30%. Portanto, seus gastos estão dentro da margem recomendada."
  
  if gastos_educacao > valor_ideal_educacao:
    educacao = f"O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {valor_ideal_educacao}."
  else:
    educacao = f"O máximo recomendado é de 20%. Portanto, seus gastos estão dentro da margem recomendada."

  if gastos_transporte > valor_ideal_transporte:
    transporte = f"O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {valor_ideal_transporte}." 
  else:
    transporte = f"O máximo recomendado é de 15%. Portanto, seus gastos estão dentro da margem recomendada."
  
  diagnostico = f"\n\nDe acordo com os valores informados;  \n"
  diagnostico += f"Seus gastos totais com moradia comprometem {percentual_real_gastos_moradia}% da sua renda. {moradia}\n"
  diagnostico += f"Seus gastos totais com educação comprometem {percentual_real_gastos_educacao} % da sua renda. {educacao}\n"
  diagnostico += f"Seus gastos totais com transporte comprometem {percentual_real_gastos_transporte} % da sua renda. {transporte}\n"
  print(diagnostico)
  
renda_total_mensal = float(input("Informe sua renda mensal: R$ "))
gastos_moradia = float(input("Informe seu gasto total com moradia: R$ "))
gastos_educacao = float(input("Informa seu gasto total com educação: R$ "))
gastos_transporte = float(input("Informe seu gasto total com transporte: R$ "))
diagnosticar_percentual_comprometido(renda_total_mensal, gastos_moradia, gastos_educacao, gastos_transporte)







