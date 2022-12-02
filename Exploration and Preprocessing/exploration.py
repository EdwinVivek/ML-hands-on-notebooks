import pandas as pd
import os

def do_exploration():
    #mydata = pd.read_csv('C:/Users/EdwinVivekN/AppData/Local/Programs/Python/Python37-32/myscripts/data/sample.xlsx')
    mydata = pd.read_csv(os.getcwd() + '\\data\\train_loanpred.xlsx')
    return mydata

loan = pd.read_csv(os.getcwd() + '\\data\\train_loanpred.csv')


def getminmax(col):
    minrow = col.idxmin()
    maxrow = col.idxmax()
    minmax = pd.concat([loan.loc[minrow], loan.loc[maxrow]], axis=1, keys=['Min:{0}'.format(minrow), 'Max:{0}'.format(maxrow)])
    return minmax

for col in loan.columns:
	if loan[col].dtypes == 'object':
		unique_cat = len(loan[col].unique())
		print('Column {col} has {unique} unique categories'.format(col=col, unique=unique_cat))

#correlation
pear_corr = loan.corr(method='pearson') #kendall,spearman
sns.heatmap(pear_corr, square=True, linewidths=.5, annot=True)


#handle missing value
loan[loan.isnull().any(axis=1)]  #row with null values, len()
len(loan[loan.LoanAmount.isnull()]) #null column count
loan.loc[loan.LoanAmount.isnull(),:].count() #null values of other columns w.r.t a null column

total = loan.isnull().sum().sort_values(ascending=False)
percent = (loan.isnull().sum()/ loan.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total','Percentage'])
missing_data
loan2 = loan.drop(missing_data[missing_data['Total'] > 1].index, axis=1)
loan2 = loan2.reset_index(drop=True)


from sklearn.impute import SimpleImputer


#impute missing value
means = loan.groupby(by='Property_Area')['LoanAmount'].mean()
map_means = means.to_dict()
idx_loanamt = loan.loc[loan.LoanAmount.isna()].index
loan.loc[idx_loanamt, 'LoanAmount'] = loan.loc[idx_loanamt, 'Property_Area'].map(map_means)

#skewness
loan.LoanAmount.skew()


#kutosis
loan.LoanAmount.kurt()


#outliers detection
#univariate outliers
plt.scatter(range(loan.shape[0]), np.sort(loan.ApplicantIncome.values))
loan.boxplot(column='ApplicantIncome')

#tukey iqr - outlier
q1 = np.percentile(loan.ApplicantIncome, 25)
q3 = np.percentile(loan.ApplicantIncome, 75)
iqr = q3-q1
floor = q1 - 1.5*iqr
ceil = q3+1.5*iqr
outlier_indices  = list(loan.ApplicantIncome.index[(loan.ApplicantIncome < floor) | (loan.ApplicantIncome > ceil)])
outlier_values = list(loan.ApplicantIncome[outlier_indices])

#kernel density estimation - outliers
from statsmodels.nonparametric.kde import KDEUnivariate



#z-score - outliers
zscore = np.abs(stats.zscore(loan.ApplicantIncome))
print(np.where(z > 3))

#odin - outliers
sqrt(point^2 - centroid^2) / max(points) > Threshold === True then it's an anomaly.



#feature engineering
x_tf = loan.copy()
from scipy.stats import boxcox
x_tf.LoanAmount = boxcox(x_tf.LoanAmount + 1)[0]

from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_transformed_scaled = scaler.fit_transform(x_tf)
poly = PolynomialFeatures(degree=2).fit(x_tf)
X_train_poly = poly.transform(X_train_transformed_scaled)
poly.get_feature_names()



#two way table


#z-test


#t-test


#chi sq test



#distribution
hist



