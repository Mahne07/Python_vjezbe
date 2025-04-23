def je_prost(broj):
    if broj <=1:
        return False
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return False
    return True

print(je_prost(7)) # Treba ispisati: True
print(je_prost(8)) 
