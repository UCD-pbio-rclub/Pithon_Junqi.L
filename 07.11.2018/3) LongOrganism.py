# Method 2
class LongOrganism(Organism):
    import Organism
    
    global long_levels
    long_levels = [*levels, 'Ploidy?', 'Genome size?','Around the world']
    
    def __init__(self, kingdom, clade, order, family, genus, species, common_name, ploidy, genome_size, region):
        self.kingdom = 'The kingdom is ' + kingdom
        self.clade = 'The clade is ' + clade
        self.order = 'The order is ' + order
        self.family = 'The family is ' + family
        self.genus = 'The genus is ' + genus
        self.species = 'The species is ' + species
        self.common_name = 'The commonname is ' + common_name
        self.ploidy = 'The ploidy is ' + ploidy
        self.genome_size = 'The genome size is ' + genome_size
        self.region = 'The region is ' + region
cuscuta = LongOrganism (*long_levels)
