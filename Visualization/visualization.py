#scatter
#matplot
fig, ax = plt.subplots()
for i in range(len(loan.Loan_Status)):
    ax.scatter(loan.LoanAmount[i], loan.ApplicantIncome[i], color= colors[loan['Loan_Status'][i]])

#pandas
loan.plot.scatter(x='LoanAmount', y='ApplicantIncome',c='CoapplicantIncome', colormap='viridis')

#seaborn
sns.scatterplot(x='LoanAmount', y='ApplicantIncome',hue='Loan_Status', data=loan)



#line plot
x_data = range(0, loan.shape[0])
#matplot
plt.plot(x_data, loan['ApplicantIncome'], label=loan['ApplicantIncome'])

#pandas
loan['ApplicantIncome'].plot.line()

#seaborn
sns.lineplot(x_data, 'ApplicantIncome', data=loan)



#histogram
#matplot
plt.hist(loan['ApplicantIncome'])

#pandas
loan['ApplicantIncome'].plot.hist()

#seaborn
sns.distplot(loan['ApplicantIncome'], bins=10, kde=False)



#bar
#matplot
data = loan['Property_Area'].value_counts()
plt.bar(data.index, data.values)

#pandas
loan['Property_Area'].value_counts().plot.bar()

#eaborn
sns.countplot(loan['Property_Area'])



#boxplot



#heatmap
#matplot
corr = loan.corr()
plt.imshow(corr.values)
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = plt.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")

#seaborn
sns.heatmap(loan.corr(), annot=True)
