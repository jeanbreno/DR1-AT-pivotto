def extrair_dados(caminho_arquivo):
  with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
  conteudo = conteudo.splitlines()
  rotulos = conteudo[0] 
  rotulos = rotulos.split(',')
  conteudo = conteudo[1:] 
  dados = []
  for paises_pib in conteudo:
    paises_pib = paises_pib.split(',') 
    dados.append(paises_pib) 
  return rotulos, dados
  
def escolher_pais():
  rotulos, dados = extrair_dados('/content/drive/MyDrive/Cópia de Assessment_PIBs - Planilha1.csv')
  for w in dados:
    print(w)

escolher_pais() 
