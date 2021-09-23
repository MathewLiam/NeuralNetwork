from . import Neuron, Layer
from numpy import random as nprand
from random import random

class Network:
    def __init__(self, amt_input_neurons, amt_hidden_layers, amt_hidden_neurons, amt_output_neurons):
        """Creates a new neural network

        Args:
            amt_input_neurons ([type]): [description]
            amt_hidden_layers ([type]): [description]
            amt_hidden_neurons ([type]): [description]
            amt_output_neurons ([type]): [description]
        """
        self.amt_input_neurons = amt_input_neurons
        self.amt_hidden_layers = amt_hidden_layers
        self.amt_hidden_neurons = amt_hidden_neurons
        self.amt_output_neurons = amt_output_neurons
        self.initialise_layers()
        self.initialise_neuron_weights()
        self.inspect()
        

    def initialise_layers(self):
        """Initializes the network layers.
        """
        self.inputLayer = Layer(self.amt_input_neurons, random(), None)
        hiddenLayer = Layer(self.amt_hidden_neurons, random(), None)
        
        for count in range(self.amt_hidden_layers - 1):
            hiddenLayer.nextLayer = Layer(self.amt_hidden_neurons, random(), None)
            
            if not hiddenLayer.nextLayer:
                break
            
            hiddenLayer = hiddenLayer.nextLayer
        
        hiddenLayer.nextLayer = Layer(self.amt_output_neurons, random(), None)
        self.inputLayer.nextLayer = hiddenLayer

    def initialise_neuron_weights(self):
        """Initializes the synapse weights for each neurons entry,
        """
        currentLayer = self.inputLayer
        while currentLayer:
            for neuron in currentLayer.neurons:
                currentNeuron = Neuron(neuron)
                currentNeuron.set_weights(nprand.rand(3))
            currentLayer = currentLayer.nextLayer

    def inspect(self):
        currentLayer = self.inputLayer
        print("Network")
        print("=======")
        print("Layers: ")
        while currentLayer:
            currentLayer.inspect()
            currentLayer = currentLayer.nextLayer

    
    def feed_forward(self, _inputs):
        """Adds values to the input nodes of the  network

        Args:
            _inputs (numeric): The input values for the  network.
        """
        pass