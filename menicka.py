# coding=utf8
'''
Created on 18. 9. 2018

@author: ADMIN
'''
import requests
import datetime

dny = ['pondělí',"úterý","středa","čtvrtek","pátek","sobota","neděle"]

dnes=  datetime.datetime.today().weekday()


r = requests.get("http://www.restauracevelorex.cz/")
print(vars(r))
print(r.content)
decodedconted = r.content.decode()
start=decodedconted.find("Denní nabídka")
end =decodedconted.find("Cena je uvedena za kompletní menu.")
menuvelorex = decodedconted[start:end]
#print(menuvelorex)
with open("menuvelorex.html", "w") as f:
    f.write(menuvelorex)
    


r = requests.get("http://www.napurkynce.cz/purkynka/denni-menu/")

decodedconted = r.content.decode()
#print(decodedconted)
start=decodedconted.find(dny[dnes].upper())
print(start)
end =decodedconted.find(dny[dnes+1].upper())
menupurkyne = decodedconted[start:end]

with open("menupurkyne.html", "w") as f:
    f.write(menupurkyne)

r = requests.get("http://www.cookpoint.cz")

decodedconted = r.content.decode()
#print(decodedconted)
start=decodedconted.find("Denní menu")
print(start)
end =decodedconted.find("Snídaně")
menucookpoint = decodedconted[start:end]

with open("menucookpoint.html", "w") as f:
    f.write(menucookpoint)




r = requests.get("https://www.taste-of-india.cz/#daily-menu")

decodedconted = r.content.decode()
#print(decodedconted)
dendnes = dny[dnes]
dendnes=dendnes[0].upper() +dendnes[1:]
denzitra=dny[dnes+1]
denzitra = denzitra[0].upper() + denzitra[1:]
start=decodedconted.find(dendnes)
print(start)
end =decodedconted.find(denzitra)

with open("menuindie.html", "w") as f:
    f.write(menuindie)

    
