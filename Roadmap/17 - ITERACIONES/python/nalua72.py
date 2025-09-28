#for
for i in range(1,11):
    print(i)

#while
i=1
while i <= 10:
    print(i)
    i += 1

#Recursive

def print10(i=1):
    if i <= 10:
        print(i)
        print10(i+1)
print10()

""" EXTRA """

for elm in [1,2,3,4]:
    print(elm)

for elm in (1,2,3,4):
    print(elm)

for elm in {1,2,3,4}:
    print(elm)

for elm in {1: "a",2: "b",3: "c",4: "d"}:
    print(elm)

for elm in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(elm)

print(*[elm for elm in range(1,11)], sep="\n")

for char in "Programmer":
    print(char)

for elm in reversed([1,2,3,4,5]):
    print(elm)