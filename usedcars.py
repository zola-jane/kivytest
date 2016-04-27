from car import Car


def main():
    # bus = Car(180)
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    # print(bus)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)
    print(limo)

main()


"""
1. limo = Car(100)
2. limo.add_fuel(20)
3. print(limo.fuel)
4. limo.drive(115)
5. print(limo.odometer)

"""