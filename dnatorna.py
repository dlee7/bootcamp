"""convert dna to rna"""

def rna(seq):
    """convert a DNA sequence with RNA"""

    seq = seq.upper()

    return seq.replace('T','U')
