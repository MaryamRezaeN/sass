for i in range(20,31,2):
    print(i)


def cirkel ():
    radie = int(input("Vad är radien på cirkeln?: "))
    pi = 3.14
    area = pi * radie ** 2
    omkrets = pi * radie * 2
    print(f"Reslutaten är att omkretsen är {omkrets} och arean är {area}")

cirkel()