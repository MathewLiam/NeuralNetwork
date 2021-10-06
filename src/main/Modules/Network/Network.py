"""MODULE: network - for creating networks to learn from input data"""

from random import random
from .layer import Layer

class Network:
    """Defines the Network class, used to learn and then make predictions/recommendations on a known topic"""
    LEARNING_RATE = 0.5

    def __init__(self,
                amt_input_neurons,
                amt_hidden_layers,
                amt_hidden_neurons,
                amt_output_neurons):
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
        self.output_layer = None
        self.hidden_layers = []
        self.initialise_layers()

    def initialise_layers(self):
        """Initializes the network layers.
        """
        self.input_layer = Layer(self.amt_input_neurons, 0, random(), None, True)
        hidden_layer = Layer(self.amt_hidden_neurons, self.amt_input_neurons, random(), None)
        self.hidden_layers.append(hidden_layer)
        self.input_layer.nextLayer = hidden_layer
        for _ in range(self.amt_hidden_layers - 1):
            hidden_layer.nextLayer = Layer(self.amt_hidden_neurons, self.amt_hidden_neurons, random(), None)
            if not hidden_layer.nextLayer:
                break

            hidden_layer = hidden_layer.nextLayer
            self.hidden_layers.append(hidden_layer)

        hidden_layer.nextLayer = self.output_layer = Layer(self.amt_output_neurons, self.amt_hidden_neurons, random(), None)

    def inspect(self):
        """Print string representation of the network"""
        current_layer = self.input_layer
        print("Network")
        print("=======")
        print("Layers: ")
        while current_layer:
            current_layer.inspect()
            current_layer = current_layer.nextLayer

    def feed_forward(self, _inputs):
        """Adds values to the input nodes of the  network

        Args:
            _inputs (numeric): The input values for the  network.
        """
        self.input_layer.feed_forward(_inputs)

    def train(self, training_inputs, training_outputs, amt_routines=10000):
        for _ in range(amt_routines):
            count = 0
            for x in training_inputs:
                self.feed_forward(x)

                # 1. Output neuron deltas
                pd_errors_wrt_output_neuron_total_net_input = [0] * len(self.output_layer.neurons)
                for o in range(len(self.output_layer.neurons)):

                    # ∂E/∂zⱼ
                    pd_errors_wrt_output_neuron_total_net_input[o] = self.output_layer.neurons[o].calculate_pd_error_wrt_total_net_input(training_outputs[count])

                # 3. Update output neuron weights
                for o in range(len(self.output_layer.neurons)):
                    for w_ho in range(len(self.output_layer.neurons[o].weights)):

                        # ∂Eⱼ/∂wᵢⱼ = ∂E/∂zⱼ * ∂zⱼ/∂wᵢⱼ
                        pd_error_wrt_weight = pd_errors_wrt_output_neuron_total_net_input[o] * self.output_layer.neurons[o].calculate_pd_total_net_input_wrt_weight(w_ho)

                        # Δw = α * ∂Eⱼ/∂wᵢ
                        self.output_layer.neurons[o].weights[w_ho] -= self.LEARNING_RATE * pd_error_wrt_weight

                for layer in self.hidden_layers:
                    # 2. Hidden neuron deltas
                    pd_errors_wrt_hidden_neuron_total_net_input = [0] * len(layer.neurons)
                    for h in range(len(layer.neurons)):

                        # We need to calculate the derivative of the error with respect to the output of each hidden layer neuron
                        # dE/dyⱼ = Σ ∂E/∂zⱼ * ∂z/∂yⱼ = Σ ∂E/∂zⱼ * wᵢⱼ
                        d_error_wrt_hidden_neuron_output = 0
                        for o in range(len(self.output_layer.neurons)):
                            d_error_wrt_hidden_neuron_output += pd_errors_wrt_output_neuron_total_net_input[o] * self.output_layer.neurons[o].weights[h]

                        # ∂E/∂zⱼ = dE/dyⱼ * ∂zⱼ/∂
                        pd_errors_wrt_hidden_neuron_total_net_input[h] = d_error_wrt_hidden_neuron_output * layer.neurons[h].calculate_pd_total_net_input_wrt_input()

                    # 4. Update hidden neuron weights
                    for h in range(len(layer.neurons)):
                        for w_ih in range(len(layer.neurons[h].weights)):

                            # ∂Eⱼ/∂wᵢ = ∂E/∂zⱼ * ∂zⱼ/∂wᵢ
                            pd_error_wrt_weight = pd_errors_wrt_hidden_neuron_total_net_input[h] * layer.neurons[h].calculate_pd_total_net_input_wrt_weight(w_ih)

                            # Δw = α * ∂Eⱼ/∂wᵢ
                            layer.neurons[h].weights[w_ih] -= self.LEARNING_RATE * pd_error_wrt_weight

                count += 1
