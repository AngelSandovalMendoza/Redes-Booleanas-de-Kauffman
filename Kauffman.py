import numpy as np

class BooleanNetwork:
    def __init__(self, num_nodes, connectivity, initial_state=None):
        self.num_nodes = num_nodes
        self.connectivity = connectivity
        if initial_state is None:
            self.state = np.random.choice([0, 1], size=num_nodes)  # Estado inicial aleatorio
        else:
            if len(initial_state) != num_nodes:
                raise ValueError("La longitud de la generación inicial no coincide con el número de nodos.")
            self.state = np.array(initial_state)

    def update(self):
        new_state = np.zeros(self.num_nodes, dtype=int)
        for i in range(self.num_nodes):
            neighbors = np.nonzero(self.connectivity[i])[0]  # Nodos vecinos
            inputs = self.state[neighbors]  # Valores de verdad de los nodos vecinos
            new_state[i] = self.update_node(inputs)
        self.state = new_state

    def update_node(self, inputs):
        return int(np.any(inputs))

    def run_simulation(self, steps):
        for _ in range(steps):
            print(self.state)
            self.update()

if __name__ == "__main__":
    num_nodes = int(input("Ingrese el número de nodos: "))
    connectivity = np.random.randint(2, size=(num_nodes, num_nodes))
    initial_state = input("Ingrese la generación inicial que quieres usar con 0 y 1 separados por espacios: ").split()
    initial_state = [int(x) for x in initial_state]  # Convertir la entrada a una lista de enteros
    network = BooleanNetwork(num_nodes, connectivity, initial_state)
    network.run_simulation(10)
