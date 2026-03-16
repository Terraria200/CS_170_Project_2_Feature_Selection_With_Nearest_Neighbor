import numpy as np

# Load dataset
def load_data(file):
    data = np.loadtxt(file)
    return data[:,0], data[:,1:]


# Main program
file = input("Enter dataset filename: ")
labels, features = load_data(file)

print("\nChoose algorithm")
print("1) Forward Selection")
print("2) Backward Elimination")

choice = int(input())

if choice == 1:
    forward(labels, features)
else:
    backward(labels, features)
