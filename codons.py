
codon = input('input your codon please: ')

if codon == 'AUG':
    print ('this codon is the start codon')
else:
    if codon == 'AUG' or codon == 'UAG' or codon == 'UGA':
        print ('This is a stop codon')
    print ('this codon is not the start codon')

print('This always prints.')
