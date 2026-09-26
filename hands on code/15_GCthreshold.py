import gc

class Customer:
    pass

customer1=Customer()
customer2=Customer()


print(gc.get_threshold())


# gc.set_threshold(560,20,20)


print(gc.get_threshold())


print(gc.get_count())




# import gc

# # Set a very small threshold
# gc.set_threshold(10, 10, 10)

# print("Threshold :", gc.get_threshold())
# print("Before    :", gc.get_count())

# objects = []

# for i in range(50):
#     objects.append([])

#     print(
#         "Created:", i + 1,
#         " GC count:", gc.get_count()
#     )