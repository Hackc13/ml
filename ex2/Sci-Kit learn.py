from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data`
y=iris.target
feature_names=iris.feature_names
target_names=iris.target_names
print('Feature names:',feature_names)
print('Target names:',target_names)
print('\n First 10 rows of x: \n',x[:10])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

