class Caixa:
    
    # Contructor
    def __init__(self, _nom):
        self.nom = _nom
        self.primerAtribut = 10
        self.segonAtribut = "10"
        self.contingutCaixa = []
        
    # Mètodes
    # Getters
    def getNom(self):
        return self.nom
    
    def getPrimerAtribut(self):
        return self.primerAtribut
   
    def getSegonAtribut(self):
        return self.segonAtribut
   
    # Setters
    def setNom(self, nouNom):
        self.nom = nouNom

    def setPrimerAtribut(self, nouValor1rAtribut):
        self.primerAtribut = nouValor1rAtribut
    
    def setSegonAtribut(self, nouValor2nAtribut):
        self.segonAtribut = nouValor2nAtribut

    def __str__(self):
        contingutATornar = ""
        for i in range(len(self.contingutCaixa)):
            contingutATornar.append(self.contingutCaixa[i])
        return contingutATornar

    # Altres mètodes
    def metode1(self, nouValor1rAtribut, nouValor2nAtribut):
        self.contingutCaixa.append(self.primerAtribut)
        nouValor1rAtribut += nouValor2nAtribut
        self.primerAtribut = nouValor1rAtribut
        self.primerAtribut = nouValor2nAtribut
        self.contingutCaixa.append(self.primerAtribut)
    
    def metode2(self, posicioRebuda, nouValor):
        self.contingutCaixa[posicioRebuda]+=nouValor
        self.contingutCaixa[posicioRebuda] = caixaRebuda[posicioRebuda]
    
    def metode3(posicioRebuda):
        return self.contingutCaixa[posicioRebuda]
