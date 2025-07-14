import numpy as np
from pprint import pprint

# ✅ Replace with your actual .npy file path
npy_path = 'test.npy'

# Load with pickle support
data = np.load(npy_path, allow_pickle=True)

# Show general info
print(f"✅ Loaded {npy_path} — total samples: {len(data)}\n")

# Show only the first sample
print("📦 First sample:")
print("Type:", type(data[0]))
pprint(data[0])
