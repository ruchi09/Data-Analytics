#Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np






def readMatrix(file):
    fd = open(file, 'r')
    x = list()
    y = list()
    for itemset in fd:
        a=map( int, list(itemset.strip().split(",")))
        x.append(a[1:] )
        y.append(a[0])
    return x,y






def cal_accuracy(y_test, y_pred):

	print "Confusion Matrix: \n", confusion_matrix(y_test, y_pred)

	print "Accuracy : ",  accuracy_score(y_test,y_pred)*100

	print "\n\nReport : ",	classification_report(y_test, y_pred)






if __name__=="__main__":

    X,Y = readMatrix("schedule.csv")
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
    #Create a Gaussian Classifier
    model = GaussianNB()


    # print "\n --------------------------------------------------------------------------------------------------------------"
    # print "                                TRAINING (USING GAUSSIAN MODEL)"
    # print "-----------------------------------------------------------------------------------------------------------------"
    # Train the model using the training sets
    model.fit(X, Y)

    #Predict Output

    # print "\n --------------------------------------------------------------------------------------------------------------"
    # print "                                            TESTING"
    # print "-----------------------------------------------------------------------------------------------------------------"
    predicted= model.predict(X_test)
    # print predicted



    print "\n --------------------------------------------------------------------------------------------------------------"
    print "                                    EVALUATION OF LEARNT MODEL"
    print "-----------------------------------------------------------------------------------------------------------------"
    cal_accuracy(y_test,predicted);
