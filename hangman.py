from random import randint

def leiaSona(failinimi):
    # Avab failinimega faili ja loeb kõik read järjendisse
    with open(failinimi, encoding="UTF-8") as fail:
        koikRead=fail.readlines() # Loeb failist read(sõnad) ja paneb need järjendisse
        mituRidaKokku=len(koikRead) # Mitu rida on kokku?
        # Valib suvalise numbri vahemikus 1 kuni ridade arv failis
        mitmesSõna=randint(1,mituRidaKokku)
        sona=koikRead[mitmesSõna-1]# Valib juhusliku sõna vastavalt valitud reale
       # print(koikRead)
        return sona.strip()  # Eemaldab tühikud rea algusest ja lõpust
    
def elud(sona_pikkus):
    # Tagastab elude arvu vastavalt sõna pikkusele
    if sona_pikkus <= 5:
        return 2
    elif 6 <= sona_pikkus <= 8:
        return 3
    else:
        return 4
    
def algus():
    fnimi=input("Sisesta failinimi kust sõnu valida: ")
    sona=leiaSona(fnimi)# Leitakse juhuslik sõna failist
    #print(sona)
    mangijaElud=elud(len(sona))# Arvutatakse mängija elude arv
    print("Hakkame mängima! Sul on", mangijaElud, "elu")
    leitudSona=[] # oli alguses ""
    pakutudTahed=[] # List kasutaja pakutud tähtedega
    # Loob listi '_' sümbolitest, mis tähistavad leidmata tähti
    for i in sona.strip():
        leitudSona.append('_')
    
    while mangijaElud > 0: # Kas elusid on veel?
        print("Leitud sõna:", leitudSona)
        print("Sa oled pakkunud neid tähti:", pakutudTahed)
        taht=input("Paku täht: ")
        # Kontrollib, kas kasutaja pakutud täht on juba varem pakutud
        if taht in pakutudTahed:
            print("Täht on juba pakutud. Paku midagi muud! ")
        else:
            pakutudTahed.append(taht)
        # Kas üldse on see täht sõnas olemas?
        if taht in sona: 
            print("Pakutud täht on sõnas.")
            for i in range(len(sona)): # Läbime kõik sona tähed ükshaaval
                if sona[i] == taht: # Kui täht on see õige(mida me valisime)
                    leitudSona[i] = taht #Asendame vastava koha siis tähega
            if "_" not in leitudSona: # Kontrollib, kas kõik tähed on leitud
                print("Õnnitleme, olete sõna ära arvanud!")
                break  # Lõpetab mängutsükli
        else:
            # Vähendab kasutaja elusid, kui pakutud täht ei ole sõnas
            mangijaElud -=1
            print("Pakutud täht ei ole sõnas. Sul on veel", mangijaElud, "elu")
    # Kontrollib, kas kasutajal on elusid alles
    if mangijaElud == 0:
        print("Kahjuks olete kõik elud kaotanud. Õige sõna oli:", sona)
    

# Kutsun mängu funktsiooni välja  
algus()
    
