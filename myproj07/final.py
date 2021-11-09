def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            val_list = []
            for value in args:
                if filter_fn(value):
                    val_list.append(value)
                else:
                    val_list.append(alter_value)
            return fn(*val_list)

        return inner

    return wrap


@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


print(mysum(1, 2, 3, 4, 5))  # 9
print(mymultiply(1, 2, 3, 4, 5))  # 15
