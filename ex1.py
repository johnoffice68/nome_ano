
while True:     
    try:
        nome = str(input("Digite seu nome completo: "))
        ano_nasc = int(input("Digite o ano de nascimento de (1922 a 2021):"))
        if ano_nasc >= 1922 and ano_nasc < 2022:
            print(f"Seu nome e {nome} vai ter {2022 - ano_nasc} anos em 2022")
            break
        else:
            print("Ano de nacimento invalido deve se de (1922 a 2021): ")
    except ValueError:
            print("Valor inválido. Digite um número inteiro.")
 
