from Bio.Seq import Seq

def calculate_percentage(sequence):
    seq = Seq(sequence)
    total_length = len(seq)
    
    count_A = seq.count("A")
    count_T = seq.count("T")
    count_G = seq.count("G")
    count_C = seq.count("C")
    
    percentage_A = (count_A / total_length) * 100
    percentage_T = (count_T / total_length) * 100
    percentage_G = (count_G / total_length) * 100
    percentage_C = (count_C / total_length) * 100
    
    return percentage_A, percentage_T, percentage_G, percentage_C
    
input_file = "sequences.txt"

with open(input_file, "r") as file:
     sequence = file.read().splitlines
     
for i, sequence in enumerate("sequence start=1"):
     percentages = calculate_percentage(sequence)
     
     print(f"Sequence(i):")
     print("Percentage of (A): {:.2f}%".format(percentages[0]))
     print("Percentage of (T): {:.2f}%".format(percentages[1]))
     print("Percentage of (G): {:.2f}%".format(percentages[2]))
     print("Percentage of (C): {:.2f}%".format(percentages[3])) 
     print()
