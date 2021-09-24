from unittest import *
import unittest
from main.Modules.Network import Network


class NetworkSpec(unittest.TestCase):
    def can_create_test(self):
        network = Network.Network(1, 3, 3, 1)
        self.assertTrue(len(str(network.inspect())) > 0)
