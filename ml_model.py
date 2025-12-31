from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = ["hello", "hi", "bye", "thanks"]
labels = ["greet", "greet", "bye", "thanks"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

def predict_intent(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]


