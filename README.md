# Music Genre Classifier (Streamlit Application)

This branch demonstrates how you can deploy convolutional neural network into a Heroku web application. Once you have the model (***model_architecture.json*** and ***model_weights.h5***), the following files are needed:
 * Procfile
 * .slugigonre
 * requirements.txt
 * runtime.txt
 * setup.sh

For more information on the content of each file, feel free to browse them in this branch. These are necessary for the deployment process. The following buildpacks are also needed to be added at the Heroku settings:
 * https://github.com/primaryobjects/heroku-buildpack-libsndfile.git
 * https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
 * heroku/python

Essentially, they are links/scripts that Heroku uses once your web application is deployed. The first two are for processing audio files, while the last for using the python packages in the requirements.txt file.

#### How the web applicaiton works?

Since the web application is built using Streamlit, it only requires 4 files:
 * app.py
 * model/utils.py
 * model_architecture.json
 * model_weights.h5

The app.py renders the front end side of the application where the user can upload an mp3 file. Once the user loads the file, the app will load up the model from the json and h5 file and it use the **predict_genre** function (see model/utils.py) to make an inference on the genre of the uploaded mp3 file.

Note: The Streamlit application can be run locally. Simply run the command *streamlit run app.py*.
