import pandas as pd 
import numpy as np 
from tabulate import tabulate
import matplotlib.pyplot as plt  
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy


# READ A CSV FILE
dataset = pd.read_csv("your_dataset.csv")




# ASSIGN COLUMNS AS DATA

data = dataset["Column_1"]

data = dataset[['Column_1', 'Column_2', 'Column_3', 'Column_4']]




# DROP ALL NA's

data = dataset.dropna()




#RENAMING COLUMNS
data = data.rename(columns={"oldname1":"newname1", "old2":"new2", "old3":"new3"})




#CONCAT
selected_variables = pd.concat([data[['dependent','existing_variable1']], createdvariable_1, createdvariable_2], axis=1)




# CREATING A LOG-LAGGED VARIABLE

data['ln_delta'] = np.log(data['variable']).diff()





# OLS REGRESSION
model = sm.OLS.from_formula('dependent ~ C(variable1) + C(variable2) + C(variable3)', data=data)

results = mdodel.fit()
print(results.summary)





# LOGIT REGRESSION
from sklearn import linear_model
MN_logit_model = linear_model.LogisticRegression(multi_class='multinomial', solver='lbfgs')

import statsmodels.api as sm
logit_model = sm.Logit(dependent, independent).fit()


independent_vars = ['tabordrs', 'divsords', 'divwords',
 'spgtabord', 'moslsdvs', 'moslsdvw', 'moslstab', 'orders']

estimation_sample['const'] = 1

dependent_var = 'buytabw'

logit_model = sm.Logit(estimation_sample[dependent_var],
 estimation_sample[independent_vars + ['const']]).fit()

print(logit_model.summary())



# MARGINAL EFFECTS
print(machine.summary())
print(logit_model.getmargeff().summary())





from stargazer.stargazer import Stargazer
stargazer = Stargazer([logit_model])
with open('regression_table.tex', 'w') as f:
    f.write(stargazer.render_latex())



#STARGAZER
from stargazer.stargazer import Stargazer
from IPython.core.display import HTML
independent_vars = sm.add_constant(
	selected_vars)


# CREATING DUMMIES
data['dummy1'] = np.where(data['variable']<"A number",1,0)
data['dummy2'] = np.where((data['varaible2']>="A number") & (data['variable2']<"Another number"),1,0)


year_dummies = pd.get_dummies(dataset['year']).remame(
	columns={1992:'1992',1996:'1996', 2000:'2000'}).add_prefix('year_').astype(int)

gender_dummies = pd.get_dummies(dataset['gender']).rename(
	columns={1:'male', 2:'female'}).add_prefix(gender_)astype(int)




# CREATING A COLUMN BY ADDING COLUMNS

data['aggregated'] = data['Column_1'] + data['Column_2'] + data['column_3']





# SAVING FITTED VALUES

data_fitted = data.loc[~data.index.isin(model.data.missing_row_idx)]
data_fitted.insert(len(data_fitted.columns), 'dependent_FIT', results.predict())





# SEPARATING DATA INTO TRAINING AND TESTING data

data['constant'] = 1
X_test = data.loc[data['variable']]





#CONFUSION MATRIX
cm = confusion_matrix(y_test, np.where(holdout_results['results']>=0.5,1,0))
ax=plt.subplot()
sns.heatmap(cm, annot=True, fmt='g', ax=ax); #annot=True to annotate cells, fmt ='g' to disable scientific notation

ax.set_xlabel("Predicted")
ax.set_ylabel("Observed")
ax.xaxis.set_ticklabels(["No", "Yes"])
ax.yaxis.set_ticklabels(["No", "Yes"])
ax.set_title('Confusion Matrix')
plt.show()

# CREATING BOXPLOTS
sns.boxplot(x= "obs", y = "prob", data=results,showfliers=False)
plt.xlabel('Observed')
plt.ylabel("Predicted Probability")
plt.title("Predicted Probability of Y by Observed Y")
plt.show()


# CREATING HISTOGRAM
results['dependent'] = (results['prob_y'])
sns.histplot(results['dependent'])
plt.xlabel('Observed')
plt.ylabel("Predicted Probability")
plt.title("Histogram of Predicted Y")
plt.axvline(0, color='red')
plt.show()









