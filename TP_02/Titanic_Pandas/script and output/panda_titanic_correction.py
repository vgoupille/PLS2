import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
# print(titanic)
# print(titanic.dtypes)
# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
# titanic.info()
# print(titanic.shape)
# print(titanic.head())
# print(titanic["Age"].describe())
# print(titanic.describe())
# print(titanic[["Name", "Age", "PassengerId", "Cabin"]])
# sub_df = titanic.iloc[:5,:4]
# print(type(sub_df))
# case = titanic.iloc[1,3]
# print(type(case))
survivor_filter = titanic["Survived"] == 1
age_filter = titanic["Age"] <= 25
# print(titanic.loc[survivor_filter])
print(titanic.loc[survivor_filter & age_filter])
print(titanic.query("(Age <= 25) and (Survived == 1)"))
print(titanic.loc[(titanic["Survived"] == 1) & (titanic["Age"] <= 25)])
