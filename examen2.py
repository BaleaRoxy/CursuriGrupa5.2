# problema1
# a = int(input("primul numar:"))
# b = int(input("al doilea numar:"))
# c = int(input("al treilea numar:"))
# if a==b==c:
#  suma = a + b + c
#  print("suma celor 3 numere:", suma)
# else:
#  print("numerele nu sunt egale")




# # problema2
# def stergerenumere(lista_numere):
#
#     pozitie = 3 - 1
#     index = 0
#     len_list = (len(lista_numere))
#
#
#     while len_list > 0:
#         index = (pozitie + index) % len_list
#
#
#         print(lista_numere.pop(index))
#         len_list -= 1
# lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# stergerenumere(lista1)


# problema3
# import itertools
#
# dictionar =  {
# "1": "abc",
# "2": "s",
# "3": "o",
# "4": "n",
# "5": "lm",
# "6": "jk",
# "7": "gi",
# "8": "def",
# "9": "abc"
# }
# for index in itertools.product(*[dictionar[i] for i in sorted(dictionar.keys())]):
#     print(''.join(index))
#
#
