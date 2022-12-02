#feture selection


#feature transformation


#binning


#missing value imputation


#normalization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
loan_norm = scaler.fit_transform(data_to_scale)
loan_norm.mean(axis=0)
loan_norm.std(axis=0)
loan_norm.max(axis=0)
loan_norm.min(axis=0)


#standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_to_scale = loan.copy()
loan_scaled = scaler.fit_transform(data_to_scale)
loan_scaled.mean(axis=0)
loan_scaled.std(axis=0)
loan_scaled.min(axis=0)
loan_scaled.max(axis=0)

#Robust Scaler
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler() 
data_scaled = scaler.fit_transform(data_to_scale)


#one-hot encoding/ label encoding
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Gender']= le.fit_transform(data['Gender']) 
onehotencoder = OneHotEncoder()
data = onehotencoder.fit_transform(data).toarray() 


#train-test split
from sklearn.model_selection import train_test_split
loan_train, loan_test, yloan_train, yloan_test = train_test_split(loan_df, loan_target, test_size=0.2, stratify=loan_df['Property_Area'])
print (loan_train.shape, yloan_train.shape)


#k-Fold CV
from sklearn.model_selection import KFold
kf = KFold(n_splits = 2)
for x_train, x_test in kf.split(loan_df, loan_target):
	print('XTrain:', x_train, 'XTest:', x_test)


#Train/Test splitting by Indices - 4d array
data_arr = np.random.rand(4,4,100,3)
all_indices = list(range(len(data_arr[0][0])))
x_train, x_test = train_test_split(all_indices, test_size=0.2)
train = data_arr[:,:,x_train,:]
train.shape
