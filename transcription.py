def transcription(dna_sequence):
  transcription = ""
  for base in dna_sequence:
    if base == "A":
      transcription += "T"
    elif base == "T":
      transcription += "U"
    elif base == "C":
      transcription += "G"
    elif base == "G":
      transcription += "C"
  return transcription
  
dna_sequence = "ACGTACGTACGT"
print(transcription(dna_sequence))
