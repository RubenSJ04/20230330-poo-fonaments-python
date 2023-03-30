from Pilota import Pilota


if __name__ == "__main__":
    pilota1 = Pilota("Joan")
    pilota2 = Pilota("$")
    pilota3 = Pilota("Josep")
     
    print(f"1. El nom de la pilota és {pilota1.getNom()}")
    print(f"2. El nom de la pilota és {pilota3.getNom()}")
    pilota1.setNom("Jordi")
    print(f"3. El nom de la pilota és {pilota1.getNom()}")
    print(f"4. El nom de la pilota és {pilota2.getNom()}")