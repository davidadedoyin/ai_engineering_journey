# Week 14: NLP fundamentals

## Analogy

Text is messy. A model does not read words like a human does. It needs the text converted into numbers first.

## Mon: what is NLP?

NLP stands for natural language processing. It is the field of teaching computers to work with human language.

Examples:
- sentiment analysis
- chatbots
- classification and summarization
- retrieval and question answering

## Tue: tokenization

Tokenization means breaking text into pieces such as words or subwords.

```python
text = "I love this product and it works really well"
print(text.lower().split())
```

This gives us a simple, human-readable representation of the text.

## Wed: stop words and preprocessing

Some words are frequent but not very informative, such as "the", "a", and "is". We often remove or normalize such words before modeling.

```python
import re
text = "I love this product! It works really well."
clean = re.sub(r"[^a-z0-9\s]", " ", text.lower())
print(clean.split())
```

## Thu: bag-of-words

A bag-of-words model turns each text into a count vector. Each word gets a column and the row stores counts for that document.

```python
from sklearn.feature_extraction.text import CountVectorizer

texts = ["I love this product", "this product is great"]
vectorizer = CountVectorizer()
print(vectorizer.fit_transform(texts).toarray())
print(vectorizer.get_feature_names_out())
```

## Friday challenge

Take a few short messages and build a tiny text classifier that labels them as positive, neutral, or negative.

## Saturday project

Build a smart reply assistant in `projects/month5_smart_reply_assistant/`.

## Did it stick? Repeat checklist

- I can explain what NLP means.
- I can explain tokenization.
- I can describe why preprocessing matters.
- I can explain what a bag-of-words representation is.
