import numpy as np
import random as rand

class Link:
    main_station_index = 0

    def __init__(self, size, num_of_connections):
        self.channel = np.empty(size, dtype=np.ubyte)
        self.num_of_connections = num_of_connections
        self.add_random_connections()

    def add_random_connections(self):
        self.indecies_of_connections = rand.sample(
            range(self.channel.size),
            self.num_of_connections
        )

    def print_indecies_of_connections(self):
        for i in self.indecies_of_connections:
            print(i)

    def propagate(self):
        while(True):
            


x = Link(123, 5)

x.print_indecies_of_connections()