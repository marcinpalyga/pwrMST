"""McCulloch-Pitts Neuron Implementation."""

import numpy as np


class McCullochPittsNeuron:
    """McCulloch-Pitts Neuron Model."""

    def __init__(self, n_inputs: int, threshold: float):
        """
        Initialize a McCulloch-Pitts neuron.

        Parameters:
        -----------
        n_inputs : int
            Number of input connections
        threshold : float
            Firing threshold (theta)
        """
        self.n_inputs = n_inputs
        self.threshold = threshold

    def heaviside(self, z: float) -> np.ndarray:
        """
        Heaviside step function.

        Parameters:
        -----------
        z : float or array-like
            Input value(s)

        Returns:
        --------
        int or array-like
            1 if z >= 0, else 0
        """
        return np.where(z >= 0, 1, 0)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Compute the neuron output.

        Parameters:
        -----------
        x : array-like, shape (n_inputs,) or (n_samples, n_inputs)
            Binary input(s)

        Returns:
        --------
        int or array-like
            Neuron output (0 or 1)

        Note: All weights are equal to 1 in the M-P model.
        Formula: y = H(sum(x_i) - threshold)
        """
        x = np.atleast_2d(x)
        z = np.sum(x, axis=1) - self.threshold
        output = self.heaviside(z)
        return output if len(output) > 1 else output[0]

    def truth_table(self) -> dict:
        """
        Generate the complete truth table for 2 or 3-input neuron.

        Returns:
        --------
        dict
            Dictionary with 'inputs' and 'outputs' keys
        """
        if self.n_inputs == 2:
            inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        elif self.n_inputs == 3:
            inputs = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
        else:
            raise ValueError("Truth table only implemented for 2 or 3-input neurons")

        outputs = self.forward(inputs)

        return {"inputs": inputs, "outputs": outputs}
