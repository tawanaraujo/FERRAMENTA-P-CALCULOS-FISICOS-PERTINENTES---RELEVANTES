import sys

#formula energia Potencial

def energiap_main ():
  objetivo_energiap = input("DADO DESCONHECIDO DO PROBLEMA ESTUDADO (e=ENERGIA, g=GRAVIDADE, m=MASSA, h=ALTURA):\n\n").strip().lower()

  if objetivo_energiap == "e":
    m = float(input("INSIRA A MASSA (m) DO OBJETO EM KG:\n\n"))
    g = float(input("INSIRA O VALOR DA CONSTANTE GRAVITACIONAL (g) EM m/s²:\n\n"))
    h = float(input("INSIRA A ALTURA (h) QUE O CORPO SE ENCONTRA EM RELAÇÃO AO CHÃO EM METROS:\n\n"))
    e = m * g * h
    print(f"A ENERGIA POTENCIAL GRAVITACIONAL É DE: {e:.2f} JOULES\n\n")

  elif objetivo_energiap == "m":
    g = float(input("INSIRA O VALOR DA CONSTANTE GRAVITACIONAL (g) EM m/s²:\n\n"))
    h = float(input("INSIRA A ALTURA (h) QUE O CORPO SE ENCONTRA EM RELAÇÃO AO CHÃO EM METROS:\n\n"))
    e = float(input("INSIRA O VALOR DA ENERGIA POTENCIAL GRAVITACIONAL (e) DO OBJETO, EM JOULES:\n\n"))
    m = e / (g * h)
    print (f"A MASSA DO OBJETO (m) É DE {m:.2f} KG\n\n")
    
  elif objetivo_energiap == "h":
    g = float(input("INSIRA O VALOR DA CONSTANTE GRAVITACIONAL (g) EM m/s²:\n\n"))
    e = float(input("INSIRA O VALOR DA ENERGIA POTENCIAL GRAVITACIONAL (e) DO OBJETO, EM JOULES:\n\n"))
    m = float(input("INSIRA A MASSA (m) DO OBJETO EM KG:\n\n"))
    h = e / (m * g)
    print (f"A ALTURA (h) QUE O OBJETO ESTAVA ERA DE {h:.2f} METROS")
    
  elif objetivo_energiap == "g":
    e = float(input("INSIRA O VALOR DA ENERGIA POTENCIAL GRAVITACIONAL (e) DO OBJETO, EM JOULES:\n\n"))
    m = float(input("INSIRA A MASSA (m) DO OBJETO EM KG:\n\n"))
    h = float(input("INSIRA A ALTURA (h) QUE O CORPO SE ENCONTRA EM RELAÇÃO AO CHÃO EM METROS:\n\n"))
    g = e / (m * h)
    print (f"A GRAVIDADE (g) LOCAL ERA DE {g:.2f} m/s²\n\n")
    
#formula segunda lei de Newton

def newton_main():
  objetivo_newton = input("DADO DESCONHECIDO DO PROBLEMA ESTUDADO (f=FORÇA, a=ACELERAÇÃO OU m=MASSA):\n\n").strip().lower()

  if objetivo_newton == "f":
    m = float(input("INSIRA A MASSA (m) DO OBJETO EM KG:\n\n"))
    a = float(input("INSIRA A ACELERAÇÃO (a) DO OBJETO EM m/s²:\n\n"))
    f = m * a 
    print (f"A FORÇA É DE: {f} N")

  elif objetivo_newton == "a":
    f = float(input("INSIRA A FORÇA (f) QUE ESTA SENDO EXERCIDA NO OBJETO EM NEWTONS:\n\n"))
    m = float(input("INSIRA A MASSA (m) DO OBJETO EM KG:\n\n"))
    a = f / m
    a_km = a * 3.6
    print(f"A ACELERAÇÃO É DE: {a} m/s² OU SEJA O OBJETO GANHA A CADA SEGUNDO: {a_km} km/h")

  elif objetivo_newton == "m":
    f = float(input("INSIRA A FORÇA (f) QUE ESTA SENDO EXERCIDA NO OBJETO EM NEWTONS:\n\n"))
    a = float(input("INSIRA A ACELERAÇÃO (a) DO OBJETO EM m/s²:\n\n"))
    m = f / a
    print(f"A MASSA DO OBJETO É DE: {m} KG")

  else:
    print("OPERAÇÃO INVÁLIDA TENTE NOVAMENTE!")

#formula velocidade media

def velocidade_media_main ():
  try:
    Ds_f = float(input("Deslocamento final(m):"))
    Ds_i = float(input("Deslocamento inicial(m):"))
    t_f = float(input("Tempo final(s):"))
    t_i = float(input("Tempo inicial(s):"))
  except ValueError:
    print("Por favor, digite apenas números válidos...")
    return
  if t_f<=t_i:
	  print("Os valores de tempo devem ser diferentes de zero, tente novamente")
	  return

  print("CALCULANDO VELOCIDADE MEDIA...\n")

  velocidade_media = (Ds_f-Ds_i)/(t_f-t_i)

  print(f"O objeto estudado tem velocidade média de: {velocidade_media:.2f} m/s")

aprensentação = """

\n============FERRAMENTAS ÚTEIS======================\n

[1] Velocidade Média (tempo, velocidade, distancia)
[2] Energia Potencial (Gravitacional)
[3] Segunda Lei de Newton (força, massa, aceleração
[4] Sair 

====================================================\n

"""

while True:
  print (aprensentação)
  
  opcao = input("DIGITE O NUMERO CORRESPONDENTE A FERRAMENTA:\n")

  if opcao == "1":
    velocidade_media_main()
  
  elif opcao == "2":
    energiap_main()
  
  elif opcao == "3":
    newton_main()

  elif opcao == "4":
    print("\n\nATÉ MAIS (FECHANDO CÓDIGO)")
    break
  
  else:
    print("OPÇÃO INVALIDA, TENTE NOVAMENTE!")

