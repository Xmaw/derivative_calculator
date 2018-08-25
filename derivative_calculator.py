def break_up_functions(f):
    base = ""
    pow = ""
    flag_pow = False
    for c in f:
        if flag_pow:
            pow = c
            flag_pow = False
            break

        elif c == '^':
            flag_pow = True

        else:
            base += c
    print("base:", base)
    print("pow: ", pow)

    calculate_derivative(base, pow, f)


def calculate_derivative(b, p, f):
    derivative = str(p + b)
    if int(p) > 2:
        derivative = derivative + '^' + str(int(p)-1)
    print("Derivative of ", f, " is: ", derivative)


f = input("Enter an input to calculate the derivative of: ")
break_up_functions(f)
