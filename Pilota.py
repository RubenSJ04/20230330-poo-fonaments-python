class Pilota:
    # Contructor
    def __init__(self, _nom):
        self.nom = _nom
        
    # Mètodes
    # Getters        
    def getNom(self):
        return self.nom

    # Setters        
    def setNom(self, _nom):
        self.nom = _nom

    # Retorna el contingut de l'objecte en format string
    def __str__(self):
        return f"El propietari de la pilota és {self.nom}"
