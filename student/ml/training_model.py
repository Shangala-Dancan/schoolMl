import os
import django
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

os.environ.setdefault("DJANGO_SETTINGS_MODULE","student_ml.settings")


django.setup()

from student.models import Student

students=Student.objects.all().values(
    "study_hours","attendance","previous_score","result"
)

df=pd.DataFrame(list(students))

X=df[["study_hours","attendance","previous_score"]]

Y=df["result"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)


model=RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,Y_train)

prediction=model.predict(X_test)

print("Accuracy",accuracy_score(Y_test,prediction))

print(classification_report(Y_test,prediction))


joblib.dump(model,"student/ml/student_model.pkl")


print("Model trained succefully")

