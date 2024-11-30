from rdkit import Chem
import pandas as pd
from rdkit.Chem import Draw, Descriptors
from PIL import Image

testosterone_smiles = 'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=CC(=O)CC[C@]34C'
mol = Chem.MolFromSmiles(testosterone_smiles)

for atom in mol.GetAtoms():
    atom.SetProp("molAtomMapNUmber", str(atom.GetIdx()))

Draw.MolToFile(mol, 'output_prop.png')

for atom in mol.GetAtoms():
    print(atom.GetIdx(),',',
          atom.GetAtomicNum(),',',
          atom.GetIsAromatic(),',',
          atom.GetSymbol())
          
for bond in mol.GetBonds():
    print(bond.GetBeginAtomIdx(),',',
          bond.GetEndAtomIdx(),',',
          bond.GetBondType())
        
        
df = pd.DataFrame({
     'Atom Index': [atom.GEtIdx() for atom in mol.GetAtoms()],
     'Atomic Number': [atom.GetAtomicNum() for atom in mol.GetAtoms()],
     'Is Aromatic': [atom.GetIsAromatic() for atom in mol.GetAtoms()],
     'Atomic SYmbol': [atom.GetSymbol() for atom in mol.GetAtoms()]
})

df.to_excel('testosterone_atoms.xlsx', index=False)     
