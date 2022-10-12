import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
seed=1234
num_samples=50
def generate_data():
    x=np.array(range(num_samples))
    #print(x)
    random_noise=np.random.uniform(-10,20,size=num_samples)
    print(random_noise)
generate_data()
