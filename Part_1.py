import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

def importdata(): 
    df=pd.read_csv('Biomechanical_Data_2Classes.csv', header = None) 
      
    # Printing the dataswet shape 
    print ("Dataset Length: ", len(df)) 
    print ("Dataset Shape: ", df.shape) 
      
    # Printing the dataset obseravtions 
    print ("Dataset: ",df.head()) 
    return df

# Function to split the dataset 
def splitdataset(df):

	# Separating the target variable 
	independent=df.iloc[1:,0:6].values
	dependent=df.iloc[1:,[6]].values
	# Splitting the dataset into train and test 
	x_train,x_test,y_train,y_test=train_test_split(independent,dependent,test_size=70,random_state=100)
	return independent, dependent, x_train, x_test, y_train, y_test 


# Function to perform training with entropy with minimum 8 records per leaf node. 
def DTE_with_min_records(x_train, x_test, y_train): 
  
    # Decision tree with entropy 
	clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, min_samples_leaf=32)  #change the value of min_samples_leaf to compare the models 
	# Performing training 
	clf_entropy.fit(x_train, y_train) 
	return clf_entropy


	

# Function to perform training with giniIndex. 
def DTG_with_min_records(x_train, x_test, y_train): 
  
    # Creating the classifier object 
	clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, min_samples_leaf=32)  #change the value of min_samples_leaf to compare the models
    # Performing training 
	clf_gini.fit(x_train, y_train) 
	return clf_gini 

	


# Function to make predictions 
def prediction(x_test, clf_object): 
  
    # Predicton on test with giniIndex 
	y_pred = clf_object.predict(x_test) 
	print("Predicted values:") 
	print(y_pred) 
	return y_pred 
      
# Function to calculate accuracy 
def cal_accuracy(y_test, y_pred): 
      
	print("Confusion Matrix: ", confusion_matrix(y_test, y_pred)) 
	print ("Accuracy : ", accuracy_score(y_test,y_pred)*100) 
	print("Report : ", classification_report(y_test, y_pred)) 
  
# Driver code 
def main():

	#n = int(input("Enter the desired number of minimum records per node leaf:"))
	# Building Phase
	df=importdata()
	independent, dependent, x_train, x_test, y_train, y_test = splitdataset(df)
	clf_entropy = DTE_with_min_records(x_train, x_test, y_train) 
	clf_gini = DTG_with_min_records(x_train, x_test, y_train)
	

      
    # Operational Phase
      
	print("Results Using Entropy:") 
    # Prediction using entropy 
	y_pred_entropy = prediction(x_test, clf_entropy) 
	cal_accuracy(y_test, y_pred_entropy) 

	print("Results Using Gini Index:")
	# Prediction using gini 
	y_pred_gini = prediction(x_test, clf_gini) 
	cal_accuracy(y_test, y_pred_gini) 

	fig, ax = plt.subplots(figsize=(11, 11))
	tree.plot_tree(clf_entropy, class_names = True, fontsize=8)
	plt.show()

	fig, ax = plt.subplots(figsize=(11, 11))
	tree.plot_tree(clf_gini, class_names = True, fontsize=8)
	plt.show()
      
      
# Calling main function 
if __name__=="__main__": 
	main()