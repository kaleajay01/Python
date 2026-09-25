# map
numbers = [1,2,3,4,5]
result = list(map(lambda x: x*2, numbers))
print(result)

# map
prices = [100, 200, 300, 400]
discounted = list(map(lambda price: price * 0.90, prices))
print(discounted)

# filter
prices = [100, 200, 300, 400, 500, 600]
expensive = list(
    filter(lambda price: price >= 250, prices)
)
print("expensive",expensive)

