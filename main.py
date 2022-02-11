'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    prim = 1
    for i in (2, n / 2):
        while prim:
            if n % i == 0:
                prim = 0
            else:
                prim = 1
    if prim == 1:
        return True
    else:
        return False


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    prod = 1
    for x in lst:
        prod = prod * x
    return prod


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    if x * y == 0:
        return x + y
    if x > y:
        return get_cmmdc_v1(x - y, y)
    else:
        return get_cmmdc_v1(x, y - x)


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def main():
    while True:
        print('1. Verifica daca un numar este prim')
        print('2. Produsul a n numere')
        print('3. Cmmdc v1')
        print('4. Cmmdc v2')
        print('x. Iesire din program')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            n = int(input("Dati numarul: "))
            print(is_prime(n))
        elif optiune == '2':
            n = int(input("Dati nr de numere: "))
            lista = []
            for i in range(0, n):
                x = int(input("Dati un nr: "))
                lista.append(x)
            print(get_product(lista))
        elif optiune == '3':
            x = int(input("Dati x: "))
            y = int(input("Dati y: "))
            print(get_cmmdc_v1(x, y))
        elif optiune == '4':
            x = int(input("Dati x: "))
            y = int(input("Dati y: "))
            print(get_cmmdc_v2(x, y))




        elif optiune == 'x':
            break


if __name__ == '__main__':
    main()
