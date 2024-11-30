from Bio.Seq import Seq

sequence = "CACACGATCGATCGTACTACGATCTACGCATCGATCTCATCATTATG"

seq = Seq(sequence)

count_A = seq.count("A")
count_T = seq.count("T")
count_G = seq.count("G")
count_C = seq.count("C")

total_length = len(seq)
percentage_A = (count_A / total_length) * 100
percentage_T = (count_T / total_length) * 100
percentage_G = (count_G / total_length) * 100
percentage_C = (count_C / total_length) * 100

print("Percentage of (A): {:.2f}%".format(percentage_A))
print("Percentage of (T): {:.2f}%".format(percentage_T))
print("Percentage of (G): {:.2f}%".format(percentage_G))
print("Percentage of (C): {:.2f}%".format(percentage_C))
