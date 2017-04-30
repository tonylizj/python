def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(potential):
    """ (str) -> bool

    Return True if potential is a valid DNA sequence.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('jdISO')
    False

    """

    valid = True

    for ch in potential:
        if ch in 'ATCG':
            continue

        else:
            valid = False

    return valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return dna2 inserted into dna1 at index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'

    """

    return dna1[0:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """"(str) -> str

    Return the complement of the nucleotide.

    >>> get_complement('T')
    'A'

    """

    if nucleotide == 'A':
            return 'T'

    elif nucleotide == 'T':
            return 'A'

    elif nucleotide == 'C':
            return 'G'

    elif nucleotide == 'G':
            return 'C'

def get_complementary_sequence(sequence):
    """(str) -> str

    Return the complement of the nucleotide.

    >>> get_complementary_sequence("AGGCT")
    'TCCGA'

    """

    complement = ""

    for ch in sequence:
        if ch == 'A':
            complement = complement + 'T'

        elif ch == 'T':
            complement = complement + 'A'

        elif ch == 'C':
            complement = complement + 'G'

        elif ch == 'G':
            complement = complement + 'C'

    return complement
