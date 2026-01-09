#1-misol
matn = input("Matn kiriting: ")

if matn.isdigit():
    print("Matn faqat raqamlardan iborat")
else:
    print("Matnda boshqa belgilar ham bor")

#2-misol
matn = input("Matn kiriting: ")

natija = matn.replace(" ", "")
print("Bo‘sh joysiz matn:", natija)

#3-misol
matn = input("Matn kiriting: ")

print("Natija:", matn.title())

#4-misol
login = input("Login kiriting: ")

if len(login) >= 4 and login.isalnum():
    print("Login to‘g‘ri")
else:
    print("Login noto‘g‘ri")

#5-misol
parol = input("Parol kiriting: ")

harf_bor = any(c.isalpha() for c in parol)
raqam_bor = any(c.isdigit() for c in parol)

if harf_bor and raqam_bor:
    print("Parol shartlarga mos")
else:
    print("Parol shartlarga mos emas")
