from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
from PIL import Image

smiles = 'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=CC(=O)CC[C@]34C'
molecule = Chem.MolFromSmiles(smiles)

img = Draw.MolToImage(molecule, size=(400, 200))

output_file = 'output.png'

descriptors = {
    'MolecularWeight': Descriptors.MolWt(molecule),
    'NumAtoms': Descriptors.HeavyAtomCount(molecule),
    'LogP': Descriptors.MolLogP(molecule),
    'NumHAcceptors': Descriptors.NumHAcceptors(molecule),
    'NUmHDonors': Descriptors.NumHDonors(molecule),
}
    
print("Molecular Descriptors;")
for key, value in descriptors.items():
    print(f"{key}: {value}")
    
