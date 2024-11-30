from Bio.Seq import Seq

# define the dna sequence
my_dna = Seq("AGTACACTGGT")

# transcribe the dna sequence to rna
rna_sequence = my_dna.transcribe()

# print both the original dna and transcribed dna
print("Original DNA Sequence:", my_dna)
print("Transcribed DNA Sequence:", rna_sequence)
