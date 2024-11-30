from Bio.Seq import Seq

# Define the DNA sequence
dna = Seq("AGTACACTGGT")

# Find the complement of the sequence
complement = dna.complement()

# Print both the original sequence and it complement
print("Original DNA Sequence:", dna)
print("complement DNA Sequence:", complement)
