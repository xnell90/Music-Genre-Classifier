# Music Genre Classifier

This repository demonstrates how you can create a CNN to classify a song's genre, and deploy the model into a Heroku web application.

There are three branches associated to this repository:

 * **master** - contains documentation on how the convolutional neural network model was created using Keras with Tensorflow as a backend framework. It also includes python code on how the music data was collected and formatted prior to the training process of the neural network.

 * **streamlit-app-v1.0** - contains the necessary code to deploy the web application into Heroku, and includes instruction how to deploy the web application to Heroku.

 * **command-line-interface-v1.0** - contains the minimal amount of code for running the app via the terminal.

Note: master and streamlit branch can run the streamlit app locally. Simply run the command *streamlit run app.py*. To run some tests before running the application locally, or deploying the model into Heroku, run the **tests.py** file and see if there are any errors. For the link to the app see https://music-genre-classifier-app.herokuapp.com
