#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    adds = calculator.add
    subs = calculator.sub
    multi = calculator.mul
    dvd = calculator.div
    print("{:d} + {:d} = {}".format(a, b, adds(a, b)))
    print("{:d} - {:d} = {}".format(a, b, subs(a, b)))
    print("{:d} * {:d} = {}".format(a, b, multi(a, b)))
    print("{:d} / {:d} = {}".format(a, b, dvd(a, b)))
