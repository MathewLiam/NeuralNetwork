"""MODULE: layer - defines the neuron layer"""

from numpy import random as nprand
from .neuron import Neuron

class Layer:
    """Layer - defines a neuron layer"""
    def __init__(self,
                amt_neurons,
                amt_input_synapses,
                _bias,
                next_layer=None,
                is_input_layer=False):
        """Consructs a new instance of the neuron layer

        Args:
            _amtNeurons (integer): Amount of neurons in the neuron layer.
            _bias (float): Bias allows you to shift the activation function by adding a constant
            _nextLayer (Layer): The next layer in the network.
        """
        self.is_input_layer = is_input_layer
        self.bias = _bias
        self.amt_input_synapses = amt_input_synapses
        self.next_layer = next_layer
        for _ in range(amt_neurons):
            self.neurons = [Neuron(_bias, []) for k in range(amt_neurons)]
        self.initialise_neuron_weights()

    def initialise_neuron_weights(self):
        """Initializes the synapse weights for each neurons entry,
        """
        for neuron in self.neurons:
            neuron.set_weights(nprand.rand(self.amt_input_synapses))


    def feed_forward(self, _inputs):
        """
        calculate inputs of all neurons in the layer and pass to next layer
        """
        output = []
        if self.is_input_layer:
            self.next_layer.feed_forward(_inputs)
        else:
            for neuron in self.neurons:
                output.append(neuron.calculate_output(_inputs))
            if self.next_layer:
                self.next_layer.feed_forward(output)
            else:
                print("output: ", output)


    def inspect(self):
        """prints the structure of the layer"""
        print("\tBIAS: ", self.bias)
        for neuron in self.neurons:
            neuron.inspect()
