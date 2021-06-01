# Heart-Diease-API
### Title
Heart Diease Model trained using Random Forest Classifier for Usage as an API for Django project.

### ML Model Description And Resources

#### Context
This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.

#### Content
Attribute Information:
* age
* sex
* chest pain type (4 values)
* resting blood pressure
* serum cholestoral in mg/dl
* fasting blood sugar > 120 mg/dl
* resting electrocardiographic results (values 0,1,2)
* maximum heart rate achieved
* exercise induced angina
* oldpeak = ST depression induced by exercise relative to rest
* the slope of the peak exercise ST segment
* number of major vessels (0-3) colored by flourosopy
* thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
* The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

#### Dataset Link
https://www.kaggle.com/johnsmith88/heart-disease-dataset

#### How to run ML Model
* Downlaod the repository and go the Model folder.
* Now first install the python and then use the pip coomands to install all the recommended libraries 
* To open the python the file Install the jupyter notebook usinhg the following command
 > pip install jupyter-notebook
* Then direct to model folder address using cmd and type
 > Jupyter notebook
* Then in the last run the code and in the end it would generate a pickle model which will be used for the API.

### Django Project API
This django project has simple form which gets data from the user and sends it to the pickle model to get the results from the model.
#### How to Run the project
To run this project direct into 'ModelAPI' using cmd and then type the following coomands
 > python manage.py makemigrations
 > python manage.py migrate
 > python manage.py runserver

