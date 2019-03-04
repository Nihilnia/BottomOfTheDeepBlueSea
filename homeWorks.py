kelime = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

harfler = dict()

for f in kelime:

    if f.lower() not in harfler:
        harfler[f.lower()] = 1
    else:
        harfler[f.lower()] += 1

for harf, adet in harfler.items():

    print("{} harfi {} kere geçiyor...".format(harf, adet))
    print("*"*50)


#################################################################

siirOPEN = open("homework.txt", "r")
siirOKU = siirOPEN.readlines()

satirlar = list()

for f in siirOKU:
    f = f.strip(" ")
    satirlar.append(f)

basHarfler = list()

for f in satirlar:
    basHarfler.append(f[0])

print(*basHarfler)

#################################################################

mailsOPEN = open("mails.txt", "r")
mailsREAD = mailsOPEN.readlines()

lines = list()

for f in mailsREAD:
    f = f.strip()
    lines.append(f)

mails = list()

for f in lines:
    if "@" in f:
        mails.append(f)

print(*mails)

#################################################################

names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

people = dict()

for x, y in zip(names, surnames):
    people[x] = y

names.sort()
for f in names:
    print(f, people[f])