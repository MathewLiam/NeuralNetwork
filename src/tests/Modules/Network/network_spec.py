import unittest
from main.modules.network.network import Network

class network_spec(unittest.TestCase):
    def can_create_network(self):
        network = Network(2, 3, 3, 1)
        self.assertEqual(network.amt_hidden_layers, 3)
        self.assertEqual(network.amt_hidden_neurons, 3)
        self.assertEqual(network.amt_input_neurons, 2)
        self.assertEqual(network.amt_output_neurons, 1)


if __name__ == '__main__':
    unittest.main()