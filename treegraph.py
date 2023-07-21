import os


root_directory="/home/user/Documents"


def build_tree(path):
    """Build a tree of directories and files"""
    tree = {}
    for root, dirs, files in os.walk(path):
        root_node = tree
        for dir in root.split('/'):
            root_node = root_node.setdefault(dir, {})
        for file in files:
            root_node[file] = None
    return tree

def generate_dot(tree):
    """Generate DOT code for the tree, left to right"""
    dot = ['digraph Filesystem {\nrankdir=LR;']
    def visit_node(node, parent=None):
        for label, child in node.items():
            if child is None:
                dot.append('    "{}" -> "{}";'.format(parent, label))
            else:
                dot.append('    "{}" [shape=folder];'.format(label))
                if parent is not None:
                    dot.append('    "{}" -> "{}";'.format(parent, label))
                visit_node(child, parent=label)
    visit_node(tree)
    dot.append('}')
    return '\n'.join(dot)

if __name__ == '__main__':
    tree = build_tree(root_directory)
    dot = generate_dot(tree)
    print(dot)
