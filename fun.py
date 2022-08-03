def fun1(num1):
    for i in range(num1, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print('')

fun1(5)