# Chapter 4 - Fine-tuning keras models
 
## Changing optimization parameters
100xp
It's time to get your hands dirty with optimization. You'll now try optimizing a model at a very low learning rate, a very high learning rate, and a "just right" learning rate. You'll want to look at the results after running this exercise, remembering that a low value for the loss function is good.
For these exercises, we've pre-loaded the predictors and target values from your previous classification models (predicting who would survive on the Titanic). You'll want the optimization to start from scratch every time you change the learning rate, to give a fair comparison of how each learning rate did in your results. So we have created a function get_new_model() that creates an unoptimized model to optimize.
### Instructions
Import SGD from keras.optimizers.
Create a list of learning rates to try optimizing with called lr_to_test. The learning rates in it should be .000001, 0.01, and 1.
Using a for loop to iterate over lr_to_test:
Use the get_new_model()function to build a new, unoptimized model.
Create an optimizer called my_optimizer using the SGD() constructor with keyword argument lr=lr.
Compile your model. Set the optimizer parameter to be the SGD object you created above, and because this is a classification problem, use 'categorical_crossentropy'for the loss parameter.
Fit your model using the predictors and target.


## Evaluating model accuracy on validation dataset
100xp
Now it's your turn to monitor model accuracy with a validation data set. A model definition has been provided as model. Your job is to add the code to compile it and then fit it. You'll check the validation score in each epoch.
### Instructions
Compile your model using 'adam' as the optimizer and 'categorical_crossentropy' for the loss. To see what fraction of predictions are correct (the accuracy) in each epoch, specify the additional keyword argument metrics=['accuracy'] in model.compile().
Fit the model using the predictorsand target. Create a validation split of 30% (or 0.3). This will be reported in each epoch.

## Early stopping: Optimizing the optimization
100xp
Now that you know how to monitor your model performance throughout optimization, you can use early stopping to stop optimization when it isn't helping any more. Since the optimization stops automatically when it isn't helping, you can also set a high value for epochs in your call to .fit(), as Dan showed in the video.
The model you'll optimize has been specified as model. As before, the data is pre-loaded as predictors and target.
### Instructions
Import EarlyStopping from keras.callbacks.
Compile the model, once again using 'adam' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy at each epoch.
Create an EarlyStopping object called early_stopping_monitor. Stop optimization when the validation loss hasn't improved for 2 epochs by specifying the patience parameter of EarlyStopping() to be 2.
Fit the model using the predictorsand target. Specify the number of epochs to be 30 and use a validation split of 0.3. In addition, pass [early_stopping_monitor] to the callbacks parameter.

## Experimenting with wider networks
0xp
Now you know everything you need to begin experimenting with different models!
A model called model_1 has been pre-loaded. You can see a summary of this model printed in the IPython Shell. This is a relatively small network, with only 10 units in each hidden layer.
In this exercise you'll create a new model called model_2 which is similar to model_1, except it has 100 units in each hidden layer.
After you create model_2, both models will be fitted, and a graph showing both models loss score at each epoch will be shown. We added the argument verbose=False in the fitting commands to print out fewer updates, since you will look at these graphically instead of as text.
Because you are fitting two models, it will take a moment to see the outputs after you hit run, so be patient.
### Instructions
Create model_2 to replicate model_1, but use 100 nodes instead of 10 for the first two Dense layers you add with the 'relu' activation. Use 2 nodes for the Dense output layer with 'softmax' as the activation.
Compile model_2 as you have done with previous models: Using 'adam'as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
Hit 'Submit Answer' to fit both the models and visualize which one gives better results! Notice the keyword argument verbose=False in model.fit(): This prints out fewer updates, since you'll be evaluating the models graphically instead of through text.


## Adding layers to a network
100xp
You've seen how to experiment with wider networks. In this exercise, you'll try a deeper network (more hidden layers).
Once again, you have a baseline model called model_1 as a starting point. It has 1 hidden layer, with 50 units. You can see a summary of that model's structure printed out. You will create a similar network with 3 hidden layers (still keeping 50 units in each layer).
This will again take a moment to fit both models, so you'll need to wait a few seconds to see the results after you run your code.
### Instructions
Specify a model called model_2 that is like model_1, but which has 3 hidden layers of 50 units instead of only 1 hidden layer.
Use input_shape to specify the input shape in the first hidden layer.
Use 'relu' activation for the 3 hidden layers and 'softmax'for the output layer, which should have 2 units.
Compile model_2 as you have done with previous models: Using 'adam'as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
Hit 'Submit Answer' to fit both the models and visualize which one gives better results! For both models, you should look for the best val_loss and val_acc, which won't be the last epoch for that model.

## Building your own digit recognition model
0xp
You've reached the final exercise of the course - you now know everything you need to build an accurate model to recognize handwritten digits!
We've already done the basic manipulation of the MNIST dataset shown in the video, so you have X and y loaded and ready to model with. Sequential and Dense from keras are also pre-imported.
To add an extra challenge, we've loaded only 2500 images, rather than 60000 which you will see in some published results. Deep learning models perform better with more data, however, they also take longer to train, especially when they start becoming more complex.
If you have a computer with a CUDA compatible GPU, you can take advantage of it to improve computation time. If you don't have a GPU, no problem! You can set up a deep learning environment in the cloud that can run your models on a GPU. Here is a blog post by Dan that explains how to do this - check it out after completing this exercise! It is a great next step as you continue your deep learning journey.
### Instructions
Create a Sequential object to start your model. Call this model.
Add the first Dense hidden layer of 50 units to your model with 'relu'activation. For this data, the input_shape is (784,).
Add a second Dense hidden layer with 50 units and a 'relu' activation function.
Add the output layer. Your activation function should be 'softmax', and the number of nodes in this layer should be the same as the number of possible outputs in this case: 10.
Compile model as you have done with previous models: Using 'adam' as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
Fit the model using X and y using a validation_split of 0.3.

