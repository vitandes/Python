def dna_to_rna(dna):
    return "".join("U" if nucloide == "T" else nucloide for nucloide in dna)

print(dna_to_rna("UITT"))