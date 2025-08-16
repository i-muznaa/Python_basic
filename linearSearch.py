arr = [2, 4, 6, 8, 9, 10]
number = int(input("Enter a number: "))

for i in range(len(arr)):
    if arr[i] == number:
        print("Index:", i)
        break
else:
    print("Index: -1")   # runs if no break happened
