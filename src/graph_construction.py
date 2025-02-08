import networkx as nx
import pandas as pd

def build_graph(data):
    """Build a graph from drug-protein interaction data."""
    G = nx.Graph()
    for _, row in data.iterrows():
        G.add_node(row['Drug'], type='drug')
        G.add_node(row['Target'], type='protein')
        G.add_edge(row['Drug'], row['Target'], interaction=row['Interaction'])
    return G

if __name__ == "__main__":
    data = pd.read_csv("data/processed/drugbank_processed.csv")
    graph = build_graph(data)
    nx.write_gml(graph, "data/processed/drug_interaction_graph.gml")
