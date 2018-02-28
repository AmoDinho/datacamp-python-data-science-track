# Chapter 2 - Optimizing a neural network with backward propagation
 
## Coding how weight changes affect accuracy
100xp
Now you'll get to change weights in a real network and see how they affect model accuracy!
Have a look at the following neural network: 
Its weights have been pre-loaded as weights_0. Your task in this exercise is to update a single weight in weights_0 to create weights_1, which gives a perfect prediction (in which the predicted value is equal to target_actual: 3).
Use a pen and paper if necessary to experiment with different combinations. You'll use the predict_with_network() function, which takes an array of data as the first argument, and weights as the second argument.
### Instructions
Create a dictionary of weights called weights_1 where you have changed 1 weight from weights_0 (You only need to make 1 edit to weights_0 to generate the perfect prediction).
Obtain predictions with the new weights using the predict_with_network() function with input_data and weights_1.
Calculate the error for the new weights by subtracting target_actual from model_output_1.
Hit 'Submit Answer' to see how the errors compare!

## Scaling up to multiple data points
100xp
You've seen how different weights will have different accuracies on a single prediction. But usually, you'll want to measure model accuracy on many points. You'll now write code to compare model accuracies for two different sets of weights, which have been stored as weights_0 and weights_1.
input_data is a list of arrays. Each item in that list contains the data to make a single prediction.target_actuals is a list of numbers. Each item in that list is the actual value we are trying to predict.
In this exercise, you'll use the mean_squared_error() function from sklearn.metrics. It takes the true values and the predicted values as arguments.
You'll also use the preloaded predict_with_network() function, which takes an array of data as the first argument, and weights as the second argument.
### Instructions
Import mean_squared_error from sklearn.metrics.
Using a for loop to iterate over each row of input_data:
Make predictions for each row with weights_0 using the predict_with_network()function and append it to model_output_0.
Do the same for weights_1, appending the predictions to model_output_1.
Calculate the mean squared error of model_output_0 and then model_output_1 using the mean_squared_error() function. The first argument should be the actual values (target_actuals), and the second argument should be the predicted values (model_output_0 or model_output_1).


## Calculating slopes
100xp
You're now going to practice calculating slopes. When plotting the mean-squared error loss function against predictions, the slope is 2 * x * (y-xb), or 2 * input_data * error. Note that x and b may have multiple numbers (x is a vector for each data point, and b is a vector). In this case, the output will also be a vector, which is exactly what you want.
You're ready to write the code to calculate this slope while using a single data point. You'll use pre-defined weights called weights as well as data for a single point called input_data. The actual value of the target you want to predict is stored in target.
### Instructions
Calculate the predictions, preds, by multiplying weightsby the input_data and computing their sum.
Calculate the error, which is the difference between targetand preds. Notice that this error corresponds to y-xb in the gradient expression.
Calculate the slope of the loss function with respect to the prediction. To do this, you need to take the product of input_data and error and multiply that by 2.

## Improving model weights
100xp
Hurray! You've just calculated the slopes you need. Now it's time to use those slopes to improve your model. If you add the slopes to your weights, you will move in the right direction. However, it's possible to move too far in that direction. So you will want to take a small step in that direction first, using a lower learning rate, and verify that the model is improving.
The weights have been pre-loaded as weights, the actual value of the target as target, and the input data as input_data. The predictions from the initial weights are stored as preds.
### Instructions
Set the learning rate to be 0.01 and calculate the error from the original predictions. This has been done for you.
Calculate the updated weights by subtracting the product of learning_rate and slope from weights.
Calculate the updated predictions by multiplying weights_updated with input_data and computing their sum.
Calculate the error for the new predictions. Store the result as error_updated.
Hit 'Submit Answer' to compare the updated error to the original!

## Making multiple updates to weights
100xp
You're now going to make multiple updates so you can dramatically improve your model weights, and see how the predictions improve with each update.
To keep your code clean, there is a pre-loaded get_slope() function that takes input_data, target, and weights as arguments. There is also a get_mse() function that takes the same arguments. The input_data, target, and weights have been pre-loaded.
This network does not have any hidden layers, and it goes directly from the input (with 3 nodes) to an output node. Note that weights is a single array.
We have also pre-loaded matplotlib.pyplot, and the error history will be plotted after you have done your gradient descent steps.
### Instructions
Using a for loop to iteratively update weights:
Calculate the slope using the get_slope() function.
Update the weights using a learning rate of 0.01.
Calculate the mean squared error (mse) with the updated weights using the get_mse() function.
Append mse to mse_hist.
Hit 'Submit Answer' to visualize mse_hist. What trend do you notice?

