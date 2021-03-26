#importing modules
import pandas as pd
import matplotlib.pyplot as pyplot
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def predict_weather(T,H,P):
    d=[]
    d.append(T)
    d.append(H)
    d.append(P)
    #taking data from csv file
    data = pd.read_csv(r"precision_farming\weatherHistory.csv")
    # data.head(10)
    real_x = data.iloc[:,[3,4,5]].values
    # print(real_x)
    real_y=data.iloc[:,6].values
    # print(real_y)
    training_x,test_x,training_y,test_y=train_test_split(real_x,real_y,test_size=0.25,random_state=0)
    # print(training_x,test__x,training_y,test_y)
    s_c =StandardScaler()
    training_x =s_c.fit_transform(training_x)
    # print(training_x)
    test_x =s_c.fit_transform(test_x)

    cls =KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
    cls.fit(training_x,training_y)
    pred_y=cls.predict(test_x)
    accuracy=accuracy_score(test_y,pred_y)
    predicted_weather=cls.predict([d])
    print("Todays Weather Report"+str(predicted_weather))
    # print("Accuracy"+str(accuracy))
    w=predicted_weather
    a=accuracy
    return(str(predicted_weather))