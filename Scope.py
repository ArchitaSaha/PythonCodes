def outer():
    value = 9

    def inner():
        nonlocal value
        value = 0
        print('Inner :', value)

    inner()
    print('Outer :', value)

price = 100

def reset():
    # Before reset() : 100 135489520088528
    # Inside reset() : 200 135489520091792
    # After  reset() : 100 135489520088528

    # namespace = {'price' : None}
    # namespace = {'price' : 135489520091792}
    # namespace = {'price' : 135489520088528} # global price

    # global price
    price = 300
    print('Inside reset() :', price, id(price))
    # global price
    price = 200
    print('Inside reset() :', price, id(price))
    return

if __name__ == "__main__":
    # outer()

    print('Before reset() :', price, id(price))
    reset()
    print('After  reset() :', price, id(price))