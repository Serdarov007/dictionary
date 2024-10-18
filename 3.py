Telefon_belgisi = {"Anna" : "63188199",  
                    "GUrban" : "63115599",
                    "Oraz" : "62111444"}
key = input("Kimin nomeri gerek sana: ")
if key in Telefon_belgisi:
    print(key,"- yn telefon belgisi: ",Telefon_belgisi[key])
else:
    print(key,"- yn telefon belgisi yok")