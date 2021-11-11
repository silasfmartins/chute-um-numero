import random
x = random.randint(10,100)
while True:
    pergunta = int(input("Chute um número inteiro de 10 a 100: "))
    if pergunta == x:
        print("Você acertou! O número é {}".format(x))
        break
    if pergunta < x:
        print("Você chutou baixo")
    if pergunta > x:
        print("Você chutou alto")