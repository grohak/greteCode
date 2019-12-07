punktid = 0
vastus1 = input("Mis värvi on taevas? ")
õige1 = "sinine"
if (vastus1 == õige1):

    punktid = punktid + 1

vastus2 =input("Mitu päeva on nädalas ? ")
õige2 = "7"
if (vastus2 == õige2):

    punktid = punktid + 1

print("Kes on USA president? ")
print("1. Clinton")
print("2. Trump")
print("3. Obama")
vastus3 = input()
õige3 = "2"
if (vastus3 == õige3):

    punktid = punktid + 1

if (punktid == 3):

    print("Tubli, kõik õige")

else:

    print("Peaaegu! Proovi uuesti, õiged vastused: ")
    print("Taevas on "+ õige1)
    print("Nädalas on päevi "+ õige2)
    print("Presidendiks on " +õige3)
