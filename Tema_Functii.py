#####################
### Problema nr 1 ###
#####################

def my_function(var1, var2, var3, *args, **kwargs):
    print(var1 + var2 + var3)


my_function(1, 5, -3, 'abc', [12, 56, 'cad'])

"""    your_function() va returna 0.  """


def my_function2(var1, var2, var3, *args, **kwargs):
    print(var1 + var2)


my_function2(2, 4, 'abc', param_1=2)


#####################
### Problema nr 2 ###
#####################


def nr_total(n):
    if n == 0:
        return 0

    return n + nr_total(n - 1)


print(nr_total(14))


def nr_par_sau_impar(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return n + nr_par_sau_impar(n - 2)


print(nr_par_sau_impar(15))


#####################
### Problema nr 3 ###
#####################

def variabila_noastra():
    value = input("Numar introdus este: ")
    return int(value) if value.isnumeric() else 0

print(variabila_noastra())