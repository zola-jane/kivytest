from guitar import Guitar


def main():
    print("My Guitars!")
    guitar_list = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitar_list.append(Guitar(name, year, cost))
        print(guitar, "added.")
        name = input("Name: ")

    for i, guitar in enumerate(guitar_list):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".\
              format(i+1, guitar.name, guitar.year, guitar.cost, vintage_string))

main()
