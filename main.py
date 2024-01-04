import os;
from PIL import Image
import matplotlib.pyplot as plt

os.system('cls')

# LOGO
def showLogo():
  print(' _______  _______           _______  _______  _______  _______  _        ')
  print('(  ___  )(  ___  )|\     /|(  ___  )(       )(  ___  )(  ____ )| \    /\ ')
  print('| (   ) || (   ) || )   ( || (   ) || () () || (   ) || (    )||  \  / / ')
  print('| (___) || |   | || |   | || (___) || || || || (___) || (____)||  (_/ /  ')
  print('|  ___  || |   | || |   | ||  ___  || |(_)| ||  ___  ||     __)|   _ (   ')
  print('| (   ) || | /\| || |   | || (   ) || |   | || (   ) || (\ (   |  ( \ \  ')
  print('| )   ( || (_\ \ || (___) || )   ( || )   ( || )   ( || ) \ \__|  /  \ \ ')
  print('|/     \|(____\/_)(_______)|/     \||/     \||/     \||/   \__/|_/    \/ ')
  print('\nCriado por: Gabriel Palmieri | https://github.com/Gamapinha4 \n \n')                                                                     
##

#CASO NÃO EXISTA A PASTA FOTOS
def criarPastas():
  print(' ')
  if not os.path.exists('Fotos'):
      os.makedirs('Fotos')
      print(f'✅ A pasta FOTOS foi criada com sucesso.')
  else:
      print(f'❕ A pasta FOTOS já existe.')

  if not os.path.exists('Resultados'):
      os.makedirs('Resultados')
      print(f'✅ A pasta RESULTADOS foi criada com sucesso.')
  else:
      print(f'❕ A pasta RESULTADOS já existe.')
  print(' ')
##

#LEITURA DOS ARQUIVOS
def lerArquivos():

  diretorio = os.getcwd() + '/Fotos'

  arquivos = os.listdir(diretorio)
  arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(diretorio, arquivo))]

  if not arquivos:
     input('❕ Não existe nenhum arquivo dentro da pasta FOTOS.')
     exit()
  else:
    print(" ")
    for arq in arquivos:
      print(f'✅ O arquivo {arq} foi encontrado com sucesso.')
    print(" ")

##
  
def primeiraVez():
    
    diretorioFotos = os.getcwd() + '/Fotos'
    diretorioResultados = os.getcwd() + '/Resultados'

    if not os.path.exists(diretorioFotos) or not os.path.exists(diretorioResultados):
      result = input("O programa está dentro de uma pasta? (S ou N)")

      if result == 'S' or result == 's':
        criarPastas()
        input('❕ Coloque as fotos dentro da pasta antes de continuar | (Apos colocar as fotos aperte qualquer tecla) ')
      else:
        input('❕ Coloque dentro de uma pasta para começar a utilizar o programa.')
        exit()

#Verificar se existe WK  
def verificarWK():
   
   g = os.getcwd() + "/marca_grande.png"
   m = os.getcwd() + "/marca_media.png"
   p = os.getcwd() + "/marca_pequena.png"

   if os.path.exists(g) and os.path.exists(m) and os.path.exists(p):
      print(' ')
      print(f'✅ O arquivo da MARCA D AGUA foi encontrado com sucesso.')
      print(' ')
   else:
      input('❕ É necessario uma arquivo marca.png para continuar o programa.')
      exit()


##
def obterPosicaoUsuario():
    while True:
        try:
            print("\n \n❕ Escolha o local para a marca d'água: \n")
            print("1. Canto Superior Esquerdo")
            print("2. Canto Superior Direito")
            print("3. Canto Inferior Esquerdo")
            print("4. Canto Inferior Direito")
            print("5. Centro \n")
            
            escolha = int(input("Digite o número correspondente: "))

            if escolha == 1:
                return "top_left"
            elif escolha == 2:
                return "top_right"
            elif escolha == 3:
                return "bottom_left"
            elif escolha == 4:
                return "bottom_right"
            elif escolha == 5:
                return "center"
            else:
                print("\n 🛠️  Escolha inválida. Tente novamente.")

        except ValueError:
            print("\n 🛠️  Por favor, insira um número válido.")

def obterPosicaoPaste(imagem_principal, marca_dagua, local, fator=1):
    largura_principal, altura_principal = imagem_principal.size
    largura_marca_dagua, altura_marca_dagua = marca_dagua.size

    if local == "top_left":
        return (0, 0)
    elif local == "top_right":
        return (largura_principal - int(largura_marca_dagua * fator), 0)
    elif local == "bottom_left":
        return (0, altura_principal - int(altura_marca_dagua * fator))
    elif local == "bottom_right":
        return (largura_principal - int(largura_marca_dagua * fator), altura_principal - int(altura_marca_dagua * fator))
    elif local == "center":
        deslocamento_x = (largura_principal - largura_marca_dagua) // 2
        deslocamento_y = (altura_principal - altura_marca_dagua) // 2
        return (deslocamento_x, deslocamento_y)

def redimensionar_imagem(imagem, percentagem):
    largura, altura = imagem.size
    nova_largura = int(largura * percentagem / 100)
    nova_altura = int(altura * percentagem / 100)
    return imagem.resize((nova_largura, nova_altura), Image.ANTIALIAS)

def escolher_marca_dagua(largura_imagem):
    if largura_imagem >= 1000:
        return os.path.join(os.getcwd(), 'marca_grande.png')
    elif largura_imagem >= 900 and largura_imagem < 1000:
       return os.path.join(os.getcwd(), 'marca_media.png')
    else:
        return os.path.join(os.getcwd(), 'marca_pequena.png')
        
def adicionarMarcaDagua(imagem_principal_path, marca_dagua_path, saida_path):
    try:
        while(True):
          imagem_principal = Image.open(imagem_principal_path).convert("RGBA")
          imagem_principal.show()
          marca_dagua_path = escolher_marca_dagua(imagem_principal.width)
          marca_dagua = Image.open(marca_dagua_path).convert("RGBA")

          local = obterPosicaoUsuario()
          posicao = obterPosicaoPaste(imagem_principal, marca_dagua, local)

          imagem_com_marca_dagua = Image.new('RGBA', imagem_principal.size, (0, 0, 0, 0))
          imagem_com_marca_dagua.paste(imagem_principal, (0, 0))
          imagem_com_marca_dagua.paste(marca_dagua, posicao, marca_dagua)
          
          imagem_com_marca_dagua.show()

          result = input("\n 🛠️  A marca d' agua está no local correto? Lembrando que o sistema possui uma medida para escolher qual a melhor dimensão de marca d'agua para cada foto \n (S ou N) \n")

          if result.lower() == 's':
             imagem_com_marca_dagua.save(saida_path)
             imagem_com_marca_dagua.close()
             plt.close()
             break
          
    except Exception as e:
      print(f"Erro ao adicionar marca d'água: {e}")

def realizarMarcas():
  diretorio = os.path.join(os.getcwd() + "\\Fotos\\")
  marcadagua = os.getcwd() + "\\marca.png"
  saida_path = os.getcwd() + "/Resultados"

  arquivos = os.listdir(diretorio)
  arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(diretorio, arquivo))]

  for arq in arquivos:
     adicionarMarcaDagua(diretorio + arq, marcadagua, saida_path + "\\" + arq.split('.')[0] + "_with_WK" + '.png')
     print(f"\n ✅ Marca d' agua adicionada ao arquivo ({arq}) -> " + arq.split('.')[0] + "_with_WK" + '.png')
  
  print("\n \n ✅ Todos os arquivos concluidos, Aperte qualquer tecla para fechar o programa.")
  print('\n 🛠️  Criado por: Gabriel Palmieri | https://github.com/Gamapinha4 \n')     
  
#INICIO
showLogo()
primeiraVez()
lerArquivos()
verificarWK()
realizarMarcas()



                                                                                                                                                                                      


##



