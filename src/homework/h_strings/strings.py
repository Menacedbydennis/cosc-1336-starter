def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:  # Compare characters at the same index
            distance += 1
    return distance


def get_dna_complement(dna):
    complement = ""
    for nucleotide in dna:
        if nucleotide == 'A':
            complement = 'T' + complement
        elif nucleotide == 'T':
            complement = 'A' + complement
        elif nucleotide == 'C':
            complement = 'G' + complement
        elif nucleotide == 'G':
            complement = 'C' + complement
    return complement
