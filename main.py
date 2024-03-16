import graphviz

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_rec(root.left, key)
        elif key > root.key:
            root.right = self._delete_rec(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_rec(root.right, temp.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def to_graphviz(self, filename):
        graph = graphviz.Digraph(format='png')
        self._to_graphviz_rec(self.root, graph)
        graph.render(filename, view=True)

    def _to_graphviz_rec(self, root, graph):
        if root:
            graph.node(str(root.key), style='filled', fillcolor='lightblue', width='0.6', height='0.6')
            if root.left:
                graph.edge(str(root.key), str(root.left.key))
                self._to_graphviz_rec(root.left, graph)
            if root.right:
                graph.edge(str(root.key), str(root.right.key))
                self._to_graphviz_rec(root.right, graph)


def load_from_file(filename):
    tree = BinarySearchTree()
    with open(filename, 'r') as file:
        numbers = file.readlines()
        for num in numbers:
            tree.insert(int(num.strip()))
    return tree

def main():
    tree = BinarySearchTree()
    while True:
        print("\nMenú:")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde archivo")
        print("5. Convertir a binario (Graphviz)")
        print("6. Salir")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            key = int(input("Ingrese el número a insertar: "))
            tree.insert(key)
        elif choice == '2':
            key = int(input("Ingrese el número a buscar: "))
            if tree.search(key):
                print("El número está en el árbol.")
            else:
                print("El número no está en el árbol.")
        elif choice == '3':
            key = int(input("Ingrese el número a eliminar: "))
            tree.delete(key)
        elif choice == '4':
            filename = input("Ingrese la ruta del archivo: ")
            tree = load_from_file(filename)
            print("Árbol cargado desde el archivo.")
        elif choice == '5':
            filename = input("Ingrese el nombre del archivo de salida (sin extensión): ")
            tree.to_graphviz(filename)
            print(f"Árbol guardado como {filename}.png")
        elif choice == '6':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()