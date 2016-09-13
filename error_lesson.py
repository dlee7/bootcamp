import bioinfo_dicts

def one_to_three(seq):
    seq = seq.upper()

    aa_list = []
    for amino_acid in seq:
        if amino_acid in bioinfo_dicts.aa.keys():
            aa_list += [bioinfo_dicts.aa[amino_acid], '-']
        else:
            raise RuntimeError(amino_acid + ' is not a valid amino acid.')

    return ''.join(aa_list[:-1])
