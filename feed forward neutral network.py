
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])


expected_output = np.array([[0],
                            [1],
                            [1],
                            [0]])
np.random.seed(1)


W1 = np.random.rand(2, 2)   
W2 = np.random.rand(2, 1)  
B1 = np.random.rand(1, 2)   
B2 = np.random.rand(1, 1)   

# Learning rate
lr = 0.1

# Train the network
for epoch in range(10000):
    # Forward pass
    hidden_input = np.dot(inputs, W1) + B1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, W2) + B2
    output = sigmoid(final_input)

    # Calculate error
    error = expected_output - output

    # Backward pass
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden_output)

    # Update weights and biases
    W2 += hidden_output.T.dot(d_output) * lr
    B2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += inputs.T.dot(d_hidden) * lr
    B1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

# Display results
print("\nFinal Output after training:")
print(output)
print("\nRounded Output (Predicted):")
print(np.round(output))

