# #Regras de Input
# #print("Digite seu nome")
# #nome = input("Meu nome é Rafael")
# #print(nome)

# #idade = input("Digite a sua idade:")
# #print(type(idade))

# #salario = int(input('salario?='))
# #imposto = float(input("Digite o imposto = "))

# #sal = float(input("Digite um salario = "))
# #print(sal)

# #Exemplos
# print ("a quantidade de %s é de %d,mas o salário é %f" % ("Bananas", 10 ,1200.50))
# idade1 = 10
# idade2 = 12
# filho = 2
# print (" Eu tenho %d filhos,ambos de %d e %d anos" % (filho,idade1,idade2))
# print ("Eu tenho",filho,"filhos,ambos de ",idade1,"e",idade2,"anos")
# print (" Eu tenho %d filhos,ambos de %d e %d anos" % (2,10,12))
# print (" Eu tenho 2 filhos,ambos de 10 e 12 anos")

# z = 1755/111
# print("%.2f" % z)
# y = 1567/222
# print("%.2f" % y)
# #%d - inteiro 
# #%s - string = (#)
# #%f - float = (#numero com virgulas)
# #%b - bool  = (#vendadeiro ou falso)


# a = "Rafael"
# b = "Barbosa"
# print("Prezado "+a+" "+b+".Olá!")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5 , end ="")
print("+" + 10 * "-" + "+")

print("=" + 20 * "-" + "=")
print(("|" + " " * 20+ "|\n") * 2, end = "")
print("=" + 20 * "-" + "=")



print(" "*6+ "/" + "\\")
print(" "*5+ "/" + " "*2 + "\\")
print(" "*4+ "/" + " "*4 + "\\")
print(" "*3+ "/" + " "*6 + "\\")
print(" "*2+ "/" + " "*8 + "\\")
print(" "*1+ "/" + " "*10 + "\\")
print(" "*0+ "/" +""+ 11 * "_" + "_" + " "*0 + "\\")

frase="\nUm triangulo de base igual a {0} e altura igual a {1} possui area igual a {2}".format(3,4,12)
print(frase) 

linguagem = "Phyton"
print(f"\nProgramador em {linguagem}")

x = (2/3)
print(f"printado o {x}")
print(f"printado o {x:.1f}")

f=float(input("Digite a temperatura de Fahrenheit = "))
c = (5/9)*(f-32)
print(f"tempetura de Celsius é = {c:.1f}")
