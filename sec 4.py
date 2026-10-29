

a = float(input("zarfiat bak ro bego: "))

if a <= 0:
    print("zarfiat ro dorost vard kon")

b = float(input("masraf bak ro bego: "))

if b <= 0:
    print("masraf ro dorost vard kon")

c = (a / b) * 100

if c <= 0:
    print("a'daad ro dorost vaared nakardi!")

print("masafat : ", c)
