from Bio.Seq import Seq
messenger_rna = Seq("AUGGCCAUUCGUCAUCGAUCGAUCGAUGCUGC")
protein_sequence = messenger_rna.translate()
print("Protein Sequence:", protein_sequence)
