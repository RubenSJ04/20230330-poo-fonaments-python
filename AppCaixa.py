from Caixa import Caixa

if __name__ == "__main__":
    elMeuAtribut = 150
    caixaDEnters = int()
    caixaDEnters = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
    nomPropietari = "Joan"
    nom2nPropietari = "Jordi"
    

    caixa = Caixa(nomPropietari)
    print(f"1. El propietari de la caixa és {caixa.getNom()}")
    
    print(f"2. El primer atribut de la caixa d'en {caixa.getNom()} és {caixa.getPrimerAtribut()}")
    caixa.setPrimerAtribut(elMeuAtribut)
    print(f"3. El primer atribut de la caixa d'en {caixa.getNom()} és {caixa.getPrimerAtribut()}")
    caixa.metode1(12,43)
    print(f"4. El primer atribut de la caixa d'en {caixa.getNom()} és {caixa.getPrimerAtribut()}")
    print(f"5. El segon  atribut de la caixa d'en {caixa.getNom()} és {caixa.getSegonAtribut()}")
    caixa.setNom(nom2nPropietari)
    
    print(f"6. El propietari de la caixa és {caixa.getNom()}")
    
    