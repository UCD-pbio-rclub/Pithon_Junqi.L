def compare (variable, class_type):
    import Organism
    import LongOrganism
    
    if isinstance(variable, class_type) == True:
        print ('>>> The variable is an instance of the class.')
    else:
        print ('>>> The variable is NOT an instance of the class.')
