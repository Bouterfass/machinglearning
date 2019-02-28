class Data:
    """Class which define a data by :
    - his name
    - his type
    - his id_country
    - his year
<<<<<<< HEAD
    - his unit
    - her value """
    def __init__(self, state= "", id_state = "", type = "", name = "", year = "", unit = "", value = ""):
        self.name = name
        self.year = year
        self.unit = unit
        self.value = value
        self.type = type
        self.id_state = id_state
        self.state = state

    def printData(self):
        print("This is what is stored in your data: "+ str(self.state) +" " + str(self.year) +"  "+ str(self.value))
=======
    - his unite
    - her value"""

    def __init__(self,name,type,id_country,year,unite,value):
        """This is the constructor who initializes the attributes"""
        self.name=name
        self.type=type
        self.id_country
        self.year=year
        self.unite=unite
        self.value=value

    def printData(self):
        print("This is what is stored in your data: "+ self.name +" " + self.year +" "+ self.unit +" "+ self.value)

    def getName():
        return self.name

    def getYear():
        return self.year

    def getUnit():
        return self.unit

    def getValue():
        return self.value

    def getType():
        return self.type

    def getIdCountry():
        return self.id_country

    def setName(self, newname):
        self.name = newname

    def setYear(self, newyear):
        self.year = newyear

    def setUnit(self, newunit):
        self.unit = newunit

    def setValue(self, newvalue):
        self.value = newvalue
    
    def setType(self,newtype)
        self.value = newtype
    
    def setIdCountry(self,newIdCountry)
        self.id_country = newIdCountry
>>>>>>> c231e0e6786bd692b61d97996013440e0cbdb6f1
