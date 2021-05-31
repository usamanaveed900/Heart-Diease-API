from django.db import models

# Create your models here.

class predictions(models.Model):

    Gender_Choice=(
        (1,'Male'),
        (0,'Female')
    )

    Chest_Pain_Choice=(
        (0,'Typical angina'),
        (1,'Atypical angina'),
        (2,'Non-anginal pain'),
        (3,'Asymptomatic')
    )

    Resting_Electrocardiographic_Results_Choices=(
        (0,'Nothing to note'),
        (1,'ST-T Wave abnormality'),
        (2,'Possible or definite left ventricular hypertrophy')
    )

    fbs_Choice=(
        (1,'Yes'),
        (0,'No')
    )

    exang_Choices=(
        (1,'Yes'),
        (0,'No')
    )

    slope_Choices=(
        (0,'Upsloping: better heart rate with excercise(uncommon)'),
        (1,'Flatsloping: minimal change(typical healthy heart)'),
        (2,'Downsloping: signs of unhealthy heart')
    )

    thal_Choices=(
        (1,'Normal'),
        (2,'Fixed Defect'),
        (3,'Reversable')
    )

    age = models.IntegerField(choices=list(zip(range(1, 121), range(1, 121))))
    sex = models.IntegerField(choices=Gender_Choice)
    cp = models.IntegerField(choices=Chest_Pain_Choice)
    trestbps = models.IntegerField(choices=list(zip(range(1, 500), range(1, 500)))) #Resting Blood Sugar
    restecg = models.IntegerField(choices=Resting_Electrocardiographic_Results_Choices)
    chol = models.IntegerField(choices=list(zip(range(1, 1000), range(1, 1000)))) #Serum Cholestoral in mg/dl
    fbs = models.IntegerField(choices=fbs_Choice) #Fasting Blood Sugar higher than 120 mg/dl
    thalach = models.IntegerField(choices=list(zip(range(1, 300), range(1, 300)))) #Maximum Heart Rate Achieved
    exang = models.IntegerField(choices=exang_Choices)
    oldpeak = models.FloatField() #ST depression induced by exercise relative to rest
    slope = models.IntegerField(choices=slope_Choices) #Heart Rate Slope
    ca = models.IntegerField(choices=list(zip(range(0, 5), range(0, 5)))) #Number of Major Vessels Colored by Flourosopy
    thal = models.IntegerField(choices=thal_Choices) #Thalium Stress Result

    

