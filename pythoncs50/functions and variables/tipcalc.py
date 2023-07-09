def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    m=""
    for x in d:
        if(x.isnumeric()):
            m=m+x
    # print(float(m))
    return float(m)
    # TODO


def percent_to_float(p):
    # TODO
    m=""
    for x in p:
        if(x.isnumeric()):
            m=m+x
    # print(float(m)/100)
    return float(m)/100


main()