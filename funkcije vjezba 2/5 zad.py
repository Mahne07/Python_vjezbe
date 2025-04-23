def izracunaj_prosjek(ocjene):
    zbroj=sum(ocjene)

    if len(ocjene)>0:
         prosjek=zbroj/len(ocjene)
         return prosjek
    else:
        return 0

print(izracunaj_prosjek([1, 2, 3, 4, 5])) # Treba ispisati: 3.0
print(izracunaj_prosjek([]))
