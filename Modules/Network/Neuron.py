class Neuron:
    def __init__(self, _bias, _weights = []):
        """Neurons calculate output and besed on weight and bias. The output of each neuron will dictate the prediction.

        Args:
            _bias (float): Bias allows you to shift the activation function by adding a constant.
            _weight (float): The connecting weight of the synapse.
        """
        self.bias = _bias
        self.weights = _weights
        self.output = None

    def calculate_output(self, _input):
        """Calculates the output of the node, given the input.

        Args:
            input (numeric): The input value or the output of the previous node layer.

        Returns:
            float: The output of the node, given the input.
        """
        return self.output

    def simoid(self, _input):
        """[summary]

        Args:
            _input ([type]): [description]

        Returns:
            [type]: [description]
        """
        return 1 / self.weight * (-input)

    def sigmoid_derivative(self):
        """The derivative function of sigmoid

        Returns:
            [type]: [description]
        """
        return 1
    
    def dot_product(self):
        """
        Multiply the inputs by the synaptic weights + bias.
        """
        pass

    def calculate_output(self):
        pass

    def get_weights(self):
        return self.weights

    def set_weights(self, _weights):
        self.weights = _weights

    def inspect(self):
        print("\t\tbias: ", self.bias)
        print("\t\tweights: ", self.weights)