n = int(input("Enter the number of fruits: "))
fruits = []
for i in range(1, n + 1):
    fruit = input(f"Enter fruit {i}: ")
    fruits.append(fruit)
# Display all fruits
print("\n------------\n")
print("All fruits entered are:")
for fruit in fruits:
    print(fruit)