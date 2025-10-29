print("Ты пог или пог?")
print("1 пог")
print("2 не я не пог")
print("3 пог")
Pog1= int(input("Введите номер ответа: "))

print("Какая самая лучшая Oc?")
print("1 Mac Oc")
print("2 Linux")
print("3 Winda")
Pog2 = int(input("Введите номер ответа: "))

print("2+2?")
print("1 4")
print("2 8")
print("3 1")
Pog3 = int(input("Введите номер ответа: "))

good = 0
if Pog1 == 1:
   good += 1

if Pog2 == 2:
    good += 1

if Pog3 == 1:
    good += 1

Gop = (good / 3) * 100

print(f"{good} из 3")
print(round(Gop, 2), "%")