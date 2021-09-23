from . import Neuron

class Layer:
    # List of neurons in the layer.
    neurons = []
    nextLayer = None

    def __init__(self, _amtNeurons, _bias, _nextLayer):
        """Defines the Neuron layer, which could be a hidden, input or output layer of many neurons.

        Args:
            _amtNeurons (integer): Amount of neurons in the neuron layer.
            _bias (float): Bias allows you to shift the activation function by adding a constant
            _nextLayer (Layer): The next layer in the network.
        """
        self.bias = _bias
        self.nextLayer = _nextLayer
        for count in range(_amtNeurons):
            self.neurons.append(Neuron(_bias, []))

    def feed_forward(self, _inputs):
        """
        calculate inputs of all neurons in the layer and pass to next layer
        """
        pass

    def inspect(self):
        print("\tBIAS: ", self.bias)
        for neuron in self.neurons:
            Neuron(neuron).inspect()