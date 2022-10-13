import numpy as np
import pandas as pd

seed=1234
NUM_SAMPLE=50
def generate_data():
    num_samples=NUM_SAMPLE
    x=np.array(range(num_samples))
    #print(x)
    random_noise=np.random.uniform(-10,20,size=num_samples)
    #print(random_noise)  
    y=3.5*x+random_noise
    #print(y) 
    data=np.vstack((x,y)).T
    print(data)
    return data
data=generate_data()