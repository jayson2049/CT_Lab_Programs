from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

smiles = "C[C@H]1C(=O)N[C@H]2CSSC[C@H]3C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@@H](CSS[C@H](NC(=O)CNC(=O)[C@@H](NC2=O)[C@@H](C)O)C(=O)N[C@@H](CC4=CC=C(C=C4)O)C(=O)O)C(=O)N[C@@H](CSSC[C@@H](C(=O)N3)NC(=O)[C@H](CC5=CC=C(C=C5)O)NC(=O)[C@H](CC(=O)N)NC(=O)[C@H](CO)NC(=O)[C@H](CO)NC(=O)[C@H](CC(=O)N)N)C(=O)N[C@H](C(=O)N6CCC[C@H]6C(=O)N1)CC(=O)N)CC(C)C)CCC(=O)O"
mol = Chem.MolFromSmiles(smiles)

fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)

fp_list = DataStructs.BitVectToText(fp)
print(f"Fingerprint: {fp_list}")
