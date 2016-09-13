def ratio(x,y):
    """The ratio of 'x' to 'y',"""
    return x/y

def complement_base(base):
    """return the Watson_Crick complement of a base"""

    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq):
    """Compute reverse complement of a DNA sequence."""
    #Initialize empty string
    rev_comp = ''
    #loop through seq and add to rev_seq
    for base in reversed(seq):
        rev_comp += complement_base(base)
    return rev_comp


def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    return 42

def think_too_much():
    """express caesar's skepticism about Cassius."""
