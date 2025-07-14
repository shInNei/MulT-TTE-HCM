import pickle
from pprint import pprint

# === Load PKL Files ===
with open("porto_nodes_new.pkl", "rb") as f:
    porto_nodes = pickle.load(f)

with open("porto_edges_new_simplify.pkl", "rb") as f:
    porto_edges = pickle.load(f)

# === Explore porto_nodes_new.pkl ===
print("📌 porto_nodes_new.pkl (nodes):")
print(f"Total nodes: {len(porto_nodes)}")
print("Sample 5 nodes:")
pprint(dict(list(porto_nodes.items())[:5]))  # show 5 samples

# === Explore porto_edges_new_simplify.pkl ===
print("\n📌 porto_edges_new_simplify.pkl (edges):")
print(f"Total edges: {len(porto_edges)}")
print("Sample 5 edges:")
pprint(dict(list(porto_edges.items())[:5]))  # show 5 samples
