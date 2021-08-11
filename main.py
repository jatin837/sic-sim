import math as m
import os
import argparse
import re

class Node():
    def __init__(self, label, voltage=m.inf):
        self.label: int = label
        self.voltage: float = voltage
        self.connected_to: list[Node] = []
        self.type_of_component_connect_to: list[Node] = []

    def append_connection(self, other):
        self.connected_to.append(other)

    def __repr__(self):
        return f"(node-{self.label}, voltage={self.voltage}, connected_to={self.connected_to}"


class Parser():
    def __init__(self, source_path):
        self.source_path = source_path
        self.source = self.read_source()
        self.pattern = re.compile(r"^([VR]) *\((\d*)\) *\( *(\d*) *, *(\d*)\ *\)$")

    def read_source(self):
        with open(self.source_path, 'r') as f:
            return f.read();
    
    def parse(self) -> list[tuple]:
        result: list[Node] = []
        for line in self.source.split("\n"):
            if line[:2] == '--':
                # A comment. Just ignore it
                pass
            else:
                #<Type of component><Space><Value of component><Space>(label1, label2)
                m_obj = self.pattern.match(line)
                if m_obj:
                    T: str = m_obj.group(1)
                    Val: int = int(m_obj.group(2))
                    label: int = int(m_obj.group(3))
                    connected_to: int = int(m_obj.group(4))
                    result.append((T, Val, label, connected_to))

        return result


# Node(Type = V, Value = 12, Lable = 0, Connected_to = 1, 3)
# Node(Type = R, Value = 1, Lable = 1, Connected_to = 2)
# Node(Type = R, Value = 2, Lable = 2, Connected_to = 3, 1)
# Node(Type = R, Value = 3, Lable = 3, Connected_to = 0)
# Node(Type = R, Value = 4, Lable = 3, Connected_to = 0)



def get_args() -> tuple:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to input source")
    args = vars(ap.parse_args())

    ipath = os.path.abspath(args["input"])
    return ipath

def main():
    ipath: str = get_args()
    parser = Parser(ipath)
    res = parser.parse()
    print("-"*10)
    print(parser.source)
    print("-"*10)
    print(res)

if __name__ == "__main__":
    main()
