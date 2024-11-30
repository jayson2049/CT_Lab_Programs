from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image

smiles = 'C1=CC(=C(C=C1O)O)C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O.O.O'
m = Chem.MolFromSmiles(smiles)

img = Draw.MolToImage(m, size=(400, 200))

output_file = 'outpput.png'
img.save(output_file)

img.show()
