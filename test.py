def one():
    a, b = 12, 13
    c, b = a * 2, a / 2
    print(a, b, c)

def two():
    a, b = 1, 13
    print(a + b)

def three():
    a, b, c = 10, 200, 30
    p, q, r = c - 5, a + 3, b - 4
    print('a, b, c : ', a, b, c)
    print('p, q ,r : ', p, q, r)
one()
two()
three()
