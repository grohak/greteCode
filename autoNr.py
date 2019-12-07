auto = input("anna nr: ")
e3 = auto[:3]
v3 = auto[-3:]
if len(auto) == 6:
    if e3.isdigit():
        if  v3.isalpha():
            print("sobiv nr")
        else:
            print("lõpus ei ole tähed")
    else:
        print("esimesed ei ole numbrid")
else:
    print("peab 6 tähemärki")