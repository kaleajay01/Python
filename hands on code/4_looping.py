# loops - for, while. do while,

# for loop
print(f"\nfor loop: ")
for i in range(5):
    print(f"Iteration: {i}")

# while loop
print(f"\nWhile Loop: ")
i=0
while i<5:
     print(f"Iteration: {i}")
     i=i+1

# do while loop
print(f"\nDo-While Loop like simulation: ")
i=0
while True:
     print(f"Iteration: {i}")
     i=i+1
     if(i>=5):
        break
