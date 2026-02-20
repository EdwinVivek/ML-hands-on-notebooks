import pandas as pd
import os
import matplotlib.pyplot as plt

mydata = pd.read_excel(os.getcwd() + '\\data\\sample.xlsx', sheet_name= 'mysheet1', index_col=0, header=0)

mydata.head(4)
mydata.tail(2)
mydata.index
mydata.index.memory_usage()
mydata.describe(include='all')
mydata.describe(exclude=[np.number]) #[np.object]
mydata.info()
mydata.columns
mydata.dtypes
mydata.T
mydata.mean()
mydata.to_numpy()

#datetim
datedate = pd.to_datetime('24/03/2019')

#count categories
mydata['categories'].value_counts()
mydata[mydata['categories'] == 'place']

#object to categories
mydata['categories'] = mydata['categories'].astype('category')
mydata.categories
mydata['categories'].cat.categories = ['a', 'b', 'c', 'd'] #set categories
mydata['categories'].cat.set_categories(["a","b","c","d"],inplace=True) #set categories
#(or)
mydata['categories'] = pd.Categorical(mydata['categories'])

#pivot table
ptable = pd.pivot_table(mydata, index=mydata['categories'])  #aggfunc=sum
ptable.query('categories == ["place"]')

#pivot
pivot = mydata.pivot(columns=mydata['objects'], values=mydata['categories'])
pivot

#crosstab
pd.crosstab(index=mydata['objects'], columns=mydata['categories'], margins='true')


#apply
mydata.apply(np.cumsum)


#sort
mydata.sort_values("categories", axis=0, ascending='true')
mydata.sort_index(axis=0, ascending='true')


#plotting
mydata.boxplot(column='no')
mydata.cumsum()
mydata.hist(column='objects', by='no')


#concat
pieces = [mydata['categories'], mydata['no']]
df = pd.concat(pieces)
dff = pd.DataFrame(df, columns=['categories'])

#merge
pd.merge(left=mydata, right=dff, on='categories', how='inner', sort=True)

#merge asof
dff['no'] = np.array([2,4,5,6,7,8,9,10,1,3])
dff['no'] = dff['no'].astype('int64')
dff.sort_values(by='no', inplace=True)
pd.merge_asof(mydata, dff, on='no', direction='nearest') #backward,forward
         
#groupby
mydata.groupby(['categories']).count()

#treat missing values
pd.isna(mydata)  #pd.isnull
mydata.dropna(how='any')
mydata.fillna(value=5)

#selection by label
mydata.loc[mydata['no']]

#selection by position
mydata.iloc[0:3]   #3 rows
mydata.iloc[0:3,2:3] #3 rows, from col 2
mydata.iloc[:,2:3] #all rows

#categorical variable into dummy/indicator variables
pd.get_dummies(mydata, prefix=['obj', 'cat'], prefix_sep='$', columns=['objects', 'categories'], drop_first=True)


#boolean indexing

#cut func for binning
loanamt = loan.assign(lmt=pd.cut(loan.LoanAmount, [loan.LoanAmount.min(), loan.LoanAmount.mean(), loan.LoanAmount.max()], labels=['SmallLoan', 'HighLoan']))
loan2['LoanAmt'] = loanamt.lmt


#random sampling
mydata.sample(frac=0.5, replace=True)


#reset index
df = pd.DataFrame([('bird', 389.0),
                   ('bird', 24.0),
                   ('mammal', 80.5),
                   ('mammal', np.nan)],
                  index=['falcon', 'parrot', 'lion', 'monkey'],
                  columns=('class', 'max_speed'))


