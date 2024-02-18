def main():
    mass = int(input("m: "))
    en = energy(mass)
    print(en)

def energy(mass):
    c = 300000000
    en = mass * pow(c, 2)
    return en

main()