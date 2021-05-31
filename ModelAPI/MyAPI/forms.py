from django import forms

class PredictionForm(forms.Form):
    age = forms.ChoiceField(choices=list(zip(range(1, 121), range(1, 121))))
    sex = forms.ChoiceField(choices=[(1,'Male'),(0,'Female')])
    cp = forms.ChoiceField(choices=[(0,'Typical angina'),(1,'Atypical angina'),(2,'Non-anginal pain'),(3,'Asymptomatic')])
    trestbps = forms.ChoiceField(choices=list(zip(range(1, 500), range(1, 500))))
    restecg = forms.ChoiceField(choices=[(0,'Nothing to note'),(1,'ST-T Wave abnormality'),(2,'Possible or definite left ventricular hypertrophy')])
    chol = forms.ChoiceField(choices=list(zip(range(1, 1000), range(1, 1000))))
    fbs = forms.ChoiceField(choices=[(1,'Yes'),(0,'No')])
    thalach = forms.ChoiceField(choices=list(zip(range(1, 300), range(1, 300))))
    exang = forms.ChoiceField(choices=[(1,'Yes'),(0,'No')])
    oldpeak = forms.FloatField()
    slope = forms.ChoiceField(choices=[(0,'Upsloping: better heart rate with excercise(uncommon)'),(1,'Flatsloping: minimal change(typical healthy heart)'),(2,'Downsloping: signs of unhealthy heart')])
    ca = forms.ChoiceField(choices=list(zip(range(0, 5), range(0, 5))))
    thal = forms.ChoiceField(choices=[(1,'Normal'),(2,'Fixed Defect'),(3,'Reversable')])