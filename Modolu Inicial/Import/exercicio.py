
# Este código usa o módulo `random` para gerar um número aleatório entre 1 e 10. O usuário é solicitado a adivinhar esse número. Se o palpite do usuário (`escolha`) corresponder ao número gerado (`aleatorio`), uma mensagem de acerto é exibida. Caso contrário, uma mensagem de erro é mostrada.
import random

aleatorio = random.randint(1,10)
escolha = int(input("Tente acertar o número de 1 a 10"))

if aleatorio == escolha:
    print(f"Você acertou, o numero {escolha} é igual ao numero aleatorio {aleatorio}")
else:
    print(f"Infelizmente o numero {escolha} não é igual ao numero aleatório {aleatorio}")

1
    
    