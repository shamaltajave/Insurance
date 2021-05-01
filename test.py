import pickle
import numpy as np
import json

insu_model= pickle.load(open('insu_model.pickle','rb'))

def predict_charges(age,bmi,children,smoker):
    options = ['yes','no']
        
    smoker=smoker.lower()
    op_index=options.index(smoker)
    x=np.zeros(5)
    x[0]=age
    x[1]=bmi
    x[2]=children
    x[op_index]=1
    return insu_model.predict([x])[0]

#predict_charges(19, 27.90, 0, 'yes')

