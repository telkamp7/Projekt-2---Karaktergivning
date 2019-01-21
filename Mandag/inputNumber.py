
def inputNumber(prompt):
    """
    Dette script er lånt fra undervisningsmaterialet 'modules_python.pdf' 
    side 62 men indeholder ændringer.
    
    Forfatter: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    
    """
    """
    Opgaven er udelukkende udarbejdet i fælleskab.
    ANSVAR: 
    
    """
    
    
    """
    INPUTNUMBER beder brugeren om at indtaste et tal og outputter dette, 
    hvis indtastningen er korrekt.
    
    inputNumber displayer besked og venter på indtastning.
    Indtastning godtages først, når et valid tal indtastes - while loopet 
    fortstætter altså, hvis der f.eks. indtastes et bogstav.
    
    """
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num