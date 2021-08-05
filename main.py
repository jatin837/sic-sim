import math as m

class Node():
    def __init__(self, label, voltage=m.inf):
        self.label: int = label
        self.voltage: float = voltage
        self.connected_to: list[Node] = []

    def append_connection(self, other):
        self.connected_to.append(other)

    def __repr__(self):
        return f"(node-{self.label}, voltage={self.voltage}, connected_to={self.connected_to}"


class Parser():
    def __init__(self, source_path):
        self.source_path = source_path
        self.source = self.read_source()

    def read_source(self):
        with open(self.source_path, 'r') as f:
            return f.read();


