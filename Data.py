class Data:
    """Class which define a Data by :
    - his name
    - his year
    - his unit
    - her value """
    def __init__(self, name = "", year = "", unit = "", value = ""):
        self.name = name
        self.year = year
        self.unit = unit
        self.value = value

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

    def setName(self, newname):
        self.name = newname

    def setYear(self, newyear):
        self.year = newyear

    def setUnit(self, newunit):
        self.unit = newunit

    def setValue(self, newvalue):
        self.value = newvalue
