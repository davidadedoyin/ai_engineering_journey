# Week 05: Jupyter notebooks and virtual environments

## Analogy

A notebook is like a lab notebook with different pages. A virtual environment is like a separate workspace with its own set of tools, so one project does not break another.

## Mon: Jupyter notebooks

A Jupyter notebook lets you write code in cells and run them one by one. This is useful for exploring data.

Example notebook file:

- `first_notebook.ipynb`

A notebook is different from a script because a script runs from top to bottom. A notebook lets you experiment and inspect values in small steps.

## Tue: virtual environments

A virtual environment keeps dependencies separate for each project. We create one inside the repo in `.venv`.

Commands:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

After activation, install packages:

```bash
pip install -r requirements.txt
```

## Wed: installing packages

The goal is to make sure the environment can import the main data libraries without errors.

```python
import numpy, pandas, matplotlib, seaborn
print("imports OK")
```

## Thu: Titanic dataset

We can load the Titanic dataset from seaborn if the Kaggle version is not available:

```python
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
```

This is the fallback described in the roadmap. It is a public copy and is good for learning.

## Fri challenge

Create a new notebook, create a venv, install the libraries, load a new CSV or dataset, and print basic information.

## Sat project

We use the Titanic dataset for a simple EDA pass: shape, columns, dtypes, and sample rows.

## Did it stick? Repeat checklist

- I can explain the difference between a script and a notebook.
- I can create and activate a venv.
- I can install packages with pip.
- I can load a dataset and print its first rows.
