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
