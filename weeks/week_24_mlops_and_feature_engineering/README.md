# Week 24: Feature engineering and MLOps foundations

## Analogy

A trained model is one component in a longer process. A reproducible ML pipeline is like an assembly line: the same preparation steps must be applied during training and prediction, and the finished system needs checks after launch.

## Mon: feature engineering

Feature engineering turns raw inputs into useful model inputs. Examples include:

- scaling numeric measurements
- encoding categories
- extracting date or text features
- handling missing values

Choose transformations using domain knowledge and inspect what information they may expose.

## Tue: pipelines and data leakage

A scikit-learn `Pipeline` keeps transformations and model fitting together. Fit preprocessing only on the training data; otherwise, information from the test set can leak into training. Use `ColumnTransformer` when different columns need different transformations.

## Wed: evaluation and reproducibility

- Keep a held-out test set for final evaluation.
- Use cross-validation for model selection where appropriate.
- Record data and code versions, configuration, metrics, and random seeds.
- Compare against a simple baseline before adding complexity.

## Thu: MLOps after training

MLOps applies reliable software practices to ML systems:

- package and version models and preprocessing
- validate inputs and monitor errors, latency, and data changes
- watch for data or concept drift and re-evaluate performance
- use staged rollout and a rollback plan

Monitoring a data distribution is a warning signal, not proof that model quality has changed.

## Friday challenge

Run `pipeline_demo.py`. Inspect the preprocessing steps and test score. Extend the example with a new category and confirm the pipeline can transform it without being refit on the test data.

## Saturday project

Create a small reproducible classification pipeline, save its evaluation notes, and write a one-page monitoring plan covering input validation, drift signals, retraining criteria, and rollback.

## Did it stick? Repeat checklist

- I can describe why preprocessing belongs inside a fitted pipeline.
- I can explain how test-set leakage leads to misleading evaluation.
- I can distinguish data drift from measured model-quality regression.
- I can list what to version and monitor when deploying a model.
