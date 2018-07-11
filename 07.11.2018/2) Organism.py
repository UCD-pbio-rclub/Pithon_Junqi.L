# Method 2
class Organism(object):
    global levels
    levels = ['Plantae', 'Angiosperms-Eudicots-Asterids', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'C. pentagona', 'Dodder']
    def __init__(self, kingdom, clade, order, family, genus, species, common_name):
        self.kingdom = 'The kingdom is ' + kingdom
        self.clade = 'The clade is ' + clade
        self.order = 'The order is ' + order
        self.family = 'The family is ' + family
        self.genus = 'The genus is ' + genus
        self.species = 'The species is ' + species
        self.common_name = 'The commonname is ' + common_name
cuscuta = Organism (*levels)
