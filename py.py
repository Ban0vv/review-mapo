a = input()

print(len(a))
print(a[::-1])

if a[::-1] == a:
    print("Палиндром")
else:
    print("!Палиндром")