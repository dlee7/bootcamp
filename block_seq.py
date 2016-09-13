def gc_blocks(seq, block_size):
    ...:     i = 0
    ...:     block_seq = []
    ...:
    ...:     while i <= len(seq) and i + block_size  <= len(seq):
    ...:         temp_seq = seq[i:i+block_size]
    ...:         block_seq.append(temp_seq)
    ...:         i += block_size
    ...:     return tuple(block_seq)
