number = [1, 2, 3, 4, 5]

# def mapper(number):
#     return number ** 2

# print(list(map(mapper,number)))

map(
    list(
        map(
            lambda number: number ** 2,
            number,
        )
    )
)
