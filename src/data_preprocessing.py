import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

def load_data(filepath):
    """Load dataset from a file."""
    return pd.read_csv(filepath)

def generate_fingerprints(smiles):
    """Generate molecular fingerprints from SMILES."""
    mol = Chem.MolFromSmiles(smiles)
    return AllChem.GetMorganFingerprintAsBitVect(mol, 2)

def preprocess_data(data):
    """Preprocess data and generate fingerprints."""
    data['fingerprint'] = data['SMILES'].apply(generate_fingerprints)
    return data

if __name__ == "__main__":
    data = load_data("data/raw/drugbank.csv")
    processed_data = preprocess_data(data)
    processed_data.to_csv("data/processed/drugbank_processed.csv", index=False)
