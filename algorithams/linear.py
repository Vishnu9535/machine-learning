import matplotlib.pyplot as plt
import numpy as np

seed = 1234
NUM_SAMPLE = 50


def generate_data():
    num_samples = NUM_SAMPLE
    x = np.array(range(num_samples))
    # print(x)
    random_noise = np.random.uniform(-10, 20, size=num_samples)
    # print(random_noise)
    y = 3.5*x+random_noise
    # print(y)
    data = np.vstack((x, y)).T
    # print(data)
    return data


data = generate_data()
dataframe = pd.DataFrame(data, columns=["x", "y"])
# print(dataframe)
X = dataframe[["x"]].values
Y = dataframe[["y"]].values
dataframe.head()
# print(dataframe["x"])
plt.title("generated data")
plt.scatter(dataframe["x"], dataframe["y"])
# plt.show()
train_size = 0.7
val_size = 0.15
test_size = 0.15
indicis = list(range(NUM_SAMPLE))
np.random.shuffle(indicis)
# print(indicis)
X = X[indicis]
Y = Y[indicis]
train_start = 0
train_end = int(0.7*NUM_SAMPLE)
val_start = train_end
val_end = int((train_size+val_size)*NUM_SAMPLE)
# print(val_end)
test_start = val_end
x_train = X[train_start:train_end]
y_train = Y[train_start:train_end]
x_val = X[val_start:val_end]
y_val = Y[val_start:val_end]
x_test = X[test_start:]
y_test = Y[test_start:]
