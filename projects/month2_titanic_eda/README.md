# Titanic EDA

This project is a beginner-friendly exploratory data analysis of the Titanic dataset.

## Goal

We inspect the data and answer a few simple questions:
- What is the shape of the dataset?
- What columns are present?
- How many values are missing?
- What is the age distribution?

## How to run

```bash
python eda.py
```

## Real output

This output was captured from a validation run using the seaborn Titanic dataset:

```text
Shape: (891, 15)
Columns: ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone']
Missing values:
survived 0
pclass 0
sex 0
age 177
sibsp 0
parch 0
fare 0
embarked 2
class 0
who 0
adult_male 0
deck 688
embark_town 2
alive 0
alone 0
Age summary:
count    714.000000
mean      29.699118
std       14.526497
min        0.420000
25%       20.125000
50%       28.000000
75%       38.000000
max       80.000000
Saved chart: titanic_age_distribution.png
```

## Limitations

This is an introductory notebook and charting exercise. It is not a full research study and it does not cover advanced feature engineering or model tuning yet.
