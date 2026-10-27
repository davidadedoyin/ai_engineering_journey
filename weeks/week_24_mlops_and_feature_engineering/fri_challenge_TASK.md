# Friday challenge: build a preprocessing and model pipeline

## Goal

Run `pipeline_demo.py` and inspect how numeric and categorical columns are prepared before classification.

## Requirements

1. Identify the numeric imputation/scaling steps and categorical imputation/encoding steps.
2. Confirm that preprocessing is part of the estimator pipeline and is fitted with the training split.
3. Report the held-out accuracy and explain why this small synthetic result is not evidence of production performance.
4. Predict for a row containing a category that did not appear during training.

## Done when

- The script runs reproducibly and prints a held-out accuracy.
- The pipeline handles a previously unseen category.
- Your explanation covers leakage and at least one production monitoring signal.
