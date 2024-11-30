from Bio import Entrez
Entrez.email = "prithvi.s.ramar@gmail.com"
search_results = Entrez.read(Entrez.esearch(db="nucleotide",retmax=10, term="pancreatic cancer[Title] AND Homo sapiens[Organism], sort=PDAT"))
IDs = search_results["IdList"]
print("Retreived IDs:", IDs)
with open("pancreatic_cancer_sequences.txt", "w" )as output_file:
    for ID in IDs:
        try:
           sequence = Entrez.efetch(db="nucleotide", id=ID, rettype="fasta",retnode="text").read()
           output_file.write(sequence + "|n")
        except Exception as e:
           print(f"An error occured with ID (ID): (e)")
print("Sequence retreival and file writing complete.")
