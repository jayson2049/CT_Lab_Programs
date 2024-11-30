from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

def morgan_fingerprint(smile):
  mol = Chem.MolFromSmiles(smile)
  fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
  return fp

def integer_conversion(smile):
  fp=morgan_fingerprint(smile)
  fp_list = DataStructs.BitVectToText(fp)
  return fp_list

ans = 'X'
while(ans=='X'):
  inp=input("Enter the dragon: ")
  minp = integer_conversion(inp)
  mmn = morgan_fingerprint(inp)
  print("It is - ASCII: ", mmn)
  print("It is - integer conversion: ", minp)
  ans=input("More? - y(yes) or n(no): ")
  if (ans=='y'):
     continue
  else:
     break
print("FIN\n")
