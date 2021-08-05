import math as m
import os
import argparse

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
    
    def parse(self):
        for comm in self.source.split("\n"):
            if comm[:2] == '--':
                pass
            else:
                pass


def get_args() -> tuple:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to input source")
    args = vars(ap.parse_args())

    ipath = os.path.abspath(args["input"])
    return ipath

def main():
    ipath: str = get_args()
    parser = Parser(ipath)
    print("-"*10)
    print(parser.source)
    print("-"*10)

if __name__ == "__main__":
    main()
