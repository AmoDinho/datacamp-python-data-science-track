# Chapter 1 - Basics of deep learning and neural networks
 
## Coding the forward propagation algorithm
100xp
In this exercise, you'll write code to do forward propagation (prediction) for your first neural network:

Each data point is a customer. The first input is how many accounts they have, and the second input is how many children they have. The model will predict how many transactions the user makes in the next year. You will use this data throughout the first 2 chapters of this course.
The input data has been pre-loaded as input_data, and the weights are available in a dictionary called weights. The array of weights for the first node in the hidden layer are in weights['node_0'], and the array of weights for the second node in the hidden layer are in weights['node_1'].
The weights feeding into the output node are available in weights['output'].
NumPy will be pre-imported for you as np in all exercises.
### Instructions
Calculate the value in node 0 by multiplying input_data by its weights weights['node_0'] and computing their sum. This is the 1st node in the hidden layer.
Calculate the value in node 1 using input_data and weights['node_1']. This is the 2nd node in the hidden layer.
Put the hidden layer values into an array. This has been done for you.
Generate the prediction by multiplying hidden_layer_outputs by weights['output'] and computing their sum.
Hit 'Submit Answer' to print the output!


## The Rectified Linear Activation Function
0xp
As Dan explained to you in the video, an "activation function" is a function applied at each node. It converts the node's input into some output.
The rectified linear activation function (called ReLU) has been shown to lead to very high-performance networks. This function takes a single number as an input, returning 0 if the input is negative, and the input if the input is positive.
Here are some examples:
relu(3) = 3 
relu(-3) = 0 
### Instructions
Fill in the definition of the relu() function:
Use the max() function to calculate the value for the output of relu().
Apply the relu() function to node_0_input to calculate node_0_output.
Apply the relu() function to node_1_input to calculate node_1_output.


## Applying the network to many observations/rows of data
100xp
You'll now define a function called predict_with_network() which will generate predictions for multiple data observations, which are pre-loaded as input_data. As before, weightsare also pre-loaded. In addition, the relu()function you defined in the previous exercise has been pre-loaded.
### Instructions
Define a function called predict_with_network() that accepts two arguments - input_data_row and weights - and returns a prediction from the network as the output.
Calculate the input and output values for each node, storing them as: node_0_input, node_0_output, node_1_input, and node_1_output.
To calculate the input value of a node, multiply the relevant arrays together and compute their sum.
To calculate the output value of a node, apply the relu()function to the input value of the node.
Use a for loop to iterate over input_data:
Use your predict_with_network() to generate predictions for each row of the input_data - input_data_row. Append each prediction to results.


## Multi-layer neural networks
100xp
In this exercise, you'll write code to do forward propagation for a neural network with 2 hidden layers. Each hidden layer has two nodes. The input data has been preloaded as input_data. The nodes in the first hidden layer are called node_0_0 and node_0_1. Their weights are pre-loaded as weights['node_0_0'] and weights['node_0_1'] respectively.
The nodes in the second hidden layer are called node_1_0 and node_1_1. Their weights are pre-loaded as weights['node_1_0'] and weights['node_1_1'] respectively.
We then create a model output from the hidden nodes using weights pre-loaded as weights['output'].

### Instructions
Calculate node_0_0_input using its weights weights['node_0_0'] and the given input_data. Then apply the relu() function to get node_0_0_output.
Do the same as above for node_0_1_input to get node_0_1_output.
Calculate node_1_0_input using its weights weights['node_1_0'] and the outputs from the first hidden layer - hidden_0_outputs. Then apply the relu() function to get node_1_0_output.
Do the same as above for node_1_1_input to get node_1_1_output.
Calculate model_output using its weights weights['output'] and the outputs from the second hidden layer hidden_1_outputs array. Do not apply the relu() function to this output.


