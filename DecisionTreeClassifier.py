import csv
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt


# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini


# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


# Function to make predictions
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100)

    print("Report : ",
          classification_report(y_test, y_pred))

    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    print("True Positive Rate: {0}".format(tpr))
    print("False Positive Rate: {0}".format(fpr))
    auc = roc_auc_score(y_test, y_pred)
    print('AUC RF:%.3f' % auc)

    plt.plot(fpr, tpr, 'y-', label='DecisionTree AUC: %.3f' % auc)
    plt.plot([0, 1], [0, 1], 'k-', label='random')
    plt.plot([0, 0, 1, 1], [0, 1, 1, 1], 'g-', label='perfect')
    plt.legend()
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()


# Driver code
def main():
    # Building Phase
    # Reading feature_vector.csv
    with open("feature_vector.csv", 'r') as my_file:
        reader = csv.reader(my_file, delimiter=' ')
        feature_vector = list(reader)

    X = [list(map(float, lst)) for lst in feature_vector]

    # Reading label_vector.csv
    with open("label_vector.csv", 'r') as my_file:
        reader = csv.reader(my_file, delimiter=' ')
        label_vector = list(reader)

    y_temp_list = [list(map(int, lst)) for lst in label_vector]
    y = [j for sub in y_temp_list for j in sub]

    # Training and Testing the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=102)

    clf_gini = train_using_gini(X_train, X_test, y_train)
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)

    # Operational Phase
    print("Results Using Gini Index:")

    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)


# Calling main function
if __name__ == "__main__":
    main()
