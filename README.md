# Decision-Tree-Model-Analysis-Comparison
Consider the two data files. One is taken from the UCI Machine Learning Repository and contains biomechanical features of some patients. The task is to predict whether the patient is normal or abnormal (call it Data2). The second dataset splits the abnormal group into two different diagnoses (call it Data3). Both datasets have same 310 feature vectors, six features, and a class column.
### Steps in order:
- Taking Data2 and split it into randomly selected 240 training instances and remaining 70 as test instances. 
- Creating decision trees using the training set and the “minimum records per leaf node” values of 8, 16, and 32. 
- Repeating the same task for Data3 (Now the decision tree has three classes to predict). 
- For Data2, consider the attribute that is at the top of the decision tree selected by you in the first step, dropping this attribute and removing this column from the dataset.
### Comparing the results obtained in each step:
![1](https://user-images.githubusercontent.com/35270511/118573116-e5c31980-b74f-11eb-81bc-b7eb9d663758.PNG)
![2](https://user-images.githubusercontent.com/35270511/118573125-e8257380-b74f-11eb-8975-773d7072d12e.PNG)
![3](https://user-images.githubusercontent.com/35270511/118573129-ea87cd80-b74f-11eb-8110-fce1ddf7c70a.PNG)
##### Comments on decision trees shape & size difference, and different accuracy, precision & recall:

- Here the major deciding attribute is “degree_spondylolisthesis”.
- Decision tree, with 8 minimum samples in its every node, is the longest and as the minimum number of samples per each node increases, the depth of the decision trees decreases.
- The first tree, with 8 minimum samples in each node, has the least accuracy even when the decision tree extends to a longer depth than the other two, which have the same accuracy rate but better than the first one. This also indicates that the first tree is being affected by the noise of the data when it tries to train further.
- When comparing the precision for the two classes, second and third trees are better in detecting the “abnormal” class which should be our priority. Even though the first tree has the recall value of 0.93 for detecting “abnormal” class, there is not a significant difference as the other two decision trees also give the recall value of 0.88
- Since the depth of the third decision tree is less than the others, it will be suited best for this problem as it predicts with the better accuracy, better precision for detecting abnormality, and without unnecessarily increasing the no. of the nodes. Also, it does not cause overfitting.
![1](https://user-images.githubusercontent.com/35270511/118573446-93cec380-b750-11eb-9e0d-31a6e773143b.PNG)
![2](https://user-images.githubusercontent.com/35270511/118573447-94fff080-b750-11eb-943c-47618e9b6891.PNG)
![3](https://user-images.githubusercontent.com/35270511/118573449-96311d80-b750-11eb-8b75-36e205c91e87.PNG)
##### Comments on decision trees shape & size difference, and different accuracy, precision & recall:
- Here the major deciding attribute is “degree_spondylolisthesis”.
- Decision tree, with 8 minimum samples in its every node, is the longest and as the samples per each node increases, the depth of the decision trees decreases.
- The third tree, with 32 minimum samples in each node, has the least accuracy rate. The first and second ones have the same accuracy rate but differ in terms of no. of nodes. This indicates that the second tree is not overfitting the data when compared to the first one.
- This model has three classes to predict, from which, our least priority should be the “normal” class.
- When comparing the precision & recall values for the three classes, all three trees are performing similarly for “Spondylolisthesis”, but first and second trees are better for “Hernia”.
- The first decision tree is giving better recall for hernia while the second is giving better precision.
- Since the depth of the second decision tree is less than the first, not to mention that the third tree has the worst accuracy rate, the decision tree with 16 samples per each node will be suited best for this problem as it predicts with the better accuracy, and without unnecessarily increasing the no. of the nodes when compared to the first tree, which prevents overfitting.
- I will choose the second decision tree with minimum number of 16 samples per node.
##### Comparison between decision trees for data2 and decision trees for data3:
Now, for both datasets, attributes are the same, the only difference is in the class labels. In data2, we have had two classes, normal and abnormal, but in data3, we have 3 classes, normal, hernia and spondylolisthesis. So, our decision tree is working to predict one additional class.
- The major contributing attribute is the same, but the abnormal class label has been further identified into two more class labels, hernia and spondylolisthesis.
- Now comparing the decision trees with minimum 8 samples per node, we observed that the accuracy increased along with the precision and recall for the spondylolisthesis when we further specified the class labels. Even though the precision & recall for hernia is less than the ones which we had for the abnormal class in the data2 observations, accuracy has increased significantly.
- Comparing decision trees with minimum 16 samples per node, accuracy rate remained the same, and the precision & recall for normal class. Whereas, we have a significant increase in the precision and recall for the Spondylolisthesis.
- Comparing decision trees with minimum 32 samples per node, accuracy decreased significantly. Precision for the hernia is not up to par but recall value is great. Spondylolisthesis has great precision and recall with this tree. While the recall for normal class has decreased.
- From the above points, we can conclude that, with specifying the abnormal class into two more class labels, we have increased the accuracy rate of the tree with 16 minimum samples per node, with good precision and recall values for specifying spondylolisthesis class. This is due to the major deciding attribute being “degree_spondylolisthesis”.

###### Note: For this part, I have removed the attribute “degree_spondylolisthesis” as it is the top contributing attribute ‘X[5]’ in the first model.
![1](https://user-images.githubusercontent.com/35270511/118574304-258b0080-b752-11eb-8fb2-740d0d9132d4.PNG)
![2](https://user-images.githubusercontent.com/35270511/118574196-eceb2700-b751-11eb-97ee-d51c5ac8c8a7.PNG)
![3](https://user-images.githubusercontent.com/35270511/118574197-ee1c5400-b751-11eb-90e1-07166666f711.PNG)
##### Comments on decision trees shape & size difference, and different accuracy, precision & recall:
- Here the major deciding attribute is “pelvic_incidence”.
- Decision tree, with the 8 minimum samples in its each node, is the longest and as the samples per each node increases, the depth of the decision trees decreases.
- Second tree, with 16 minimum samples in each node, has the best accuracy rate. Other two have the same accuracy rate but worse than the second one.
- We see, when the nodes increased from 16 minimum samples to 8 minimum samples, the accuracy is affected, this means first tree is overfitting the data and is being affected by the noise.
- When comparing the precision for the two classes, second and third trees are better in detecting the “abnormal” class which should be our priority. Even though third has better precision than second, the difference is not much significant.
- Second tree is giving us the best results for recall.
- Since the depth of the second decision tree is less than the first one, it will be suited best for this problem as it predicts with the better accuracy, recall for abnormal without unnecessarily increasing the no. of the nodes.

The difference here is because we removed the most deciding attribute from the dataset, before it was “degree_spondylolisthesis” which contributed the most and gave us a good precision and recall for predicting abnormal class (further spondylolisthesis in part 2), and with removing that, accuracy decreased for the decision trees. But, even then, the tree with 16 minimum samples in its each node is doing better than the others here in terms of accuracy. Here the major deciding attribute is “pelvic_incidence”
