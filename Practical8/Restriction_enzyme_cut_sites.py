def find_restriction_sites(dna_sequence, recognition_sequence):
    """
    Find the restriction enzyme cut sites in a DNA sequence.
    """
    # Check if the input sequences are valid
    if not set(dna_sequence).issubset("ACGT"):
        return ("The DNA sequence contains non-standard nucleotides")
    if not set(recognition_sequence).issubset("ACGT"):
        return ("retriction enzyme recognition sequence contains non-standard nucleotides")

    # find the starting index of the recognition sequence in the DNA sequence
    sites = []
    for i in range(len(dna_sequence) - len(recognition_sequence) + 1):
        if dna_sequence[i:i + len(recognition_sequence)] == recognition_sequence:
            sites.append(i)  # return the starting index of the recognition sequence
    if not sites:
        return ("No restriction enzyme cut sites found")
    else: 
        return (f"in {dna_sequence}, the restriction enzyme cuts at {sites[0]}")

# example

dna_sequence = "AAATGCATGGAA"
recognition_sequence = "ATGCAT"
print(find_restriction_sites(dna_sequence, recognition_sequence))

