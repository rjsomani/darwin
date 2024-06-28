friend_names = []
friend_addresses = []

print("Please enter the names and addresses of 5 friends:")

name1 = input("Enter the name of friend 1: ")
address1 = input("Enter the address of friend 1: ")
friend_names.append(name1)
friend_addresses.append(address1)

name2 = input("Enter the name of friend 2: ")
address2 = input("Enter the address of friend 2: ")
friend_names.append(name2)
friend_addresses.append(address2)

name3 = input("Enter the name of friend 3: ")
address3 = input("Enter the address of friend 3: ")
friend_names.append(name3)
friend_addresses.append(address3)

name4 = input("Enter the name of friend 4: ")
address4 = input("Enter the address of friend 4: ")
friend_names.append(name4)
friend_addresses.append(address4)

name5 = input("Enter the name of friend 5: ")
address5 = input("Enter the address of friend 5: ")
friend_names.append(name5)
friend_addresses.append(address5)

print(f"\nPrinting the names and addresses:")
print(f"{friend_names[0]} lives in {friend_addresses[0]}.")
print(f"{friend_names[1]} lives in {friend_addresses[1]}.")
print(f"{friend_names[2]} lives in {friend_addresses[2]}.")
print(f"{friend_names[3]} lives in {friend_addresses[3]}.")
print(f"{friend_names[4]} lives in {friend_addresses[4]}.")