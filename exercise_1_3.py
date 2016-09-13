
def complement_base(base):
    """Returns the Watson_Crick complement of a base"""

    if base == 'A' or base == 'a':
        return 'T'
    elif base == 'T' or base == 't':
        return 'A'
    elif base == 'G' or base == 'g':
        return 'C'
    else:
        return 'G'

seq = input("enter your sequence: ")
def reverse_complement(seq):
    """Returns the reverse complement of a sequence"""
    reverse_seq = seq[::-1]
    #Initializing reverse complement sequence
    rev_complement = ''
    for base in seq:
        rev_complement += complement_base(base)
    print("the reverse complement sequence is: ",rev_complement)


    #Initialize reverse sequence
