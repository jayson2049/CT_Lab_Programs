from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import PDBWriter

smiles = 'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=CC(=O)CC[C@]34C'
m = Chem.MolFromSmiles(smiles)

m = Chem.AddHs(m)

AllChem.EmbedMolecule(m)

output_file = 'output_Hyd.pdb'
with PDBWriter(output_file) as writer:
    writer.write(m)
