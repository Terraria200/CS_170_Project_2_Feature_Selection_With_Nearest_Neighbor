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

# Leave-one-out nearest neighbor accuracy
def evaluate(labels, features, subset):

    correct = 0
    n = len(labels)

    for i in range(n):

        test = features[i, subset]
        best_dist = float("inf")
        best_label = None

        for k in range(n):
            if i != k:
                dist = np.sqrt(np.sum((test - features[k, subset])**2))
                if dist < best_dist:
                    best_dist = dist
                    best_label = labels[k]

        if best_label == labels[i]:
            correct += 1

    return correct / n * 100

# Forward Selection
def forward(labels, features):

    n = features.shape[1]
    current = []
    best_set, best_acc = [], 0

    print("\nBeginning Forward Selection\n")

    for i in range(n):

    feature, best = None, 0

        for f in range(n):

                        if f not in current:
                subset = current + [f]
                acc = evaluate(labels, features, subset)

                print(f"Using feature(s) {[x+1 for x in subset]} accuracy {acc:.2f}%")

                if acc > best:
                    best, feature = acc, f

        current.append(feature)
        print(f"Feature set {[x+1 for x in current]} best, accuracy {best:.2f}%\n")

        if best > best_acc:
            best_set, best_acc = current.copy(), best

    print(f"Finished search. Best subset {[x+1 for x in best_set]} accuracy {best_acc:.2f}%")



