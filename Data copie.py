#!/usr/bin/python3
class Data:
    """Class which define a data by :
    - his nom
    - his type
    - his unite
    - her value"""

    def __init__(self,nom,type,unite,valeur):
        """This is the constructor who initializes the attributes"""
        self.nom=nom
        self.type=type
        self.unite=unite
        self.valeur=valeur