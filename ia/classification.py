import pandas as pd
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("profile_scrape.csv")

df_label = df[:100]
annotation = [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
              1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1,
              1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
df_label['Annoted'] = annotation

df_unlabel = df[100:]

df_label["All"] = df_label["Description"].fillna('') + " " + df_label["Location"].fillna('') + " " + df_label["Post"].fillna('') + " " + df_label["Company"].fillna('')
df_unlabel["All"] = df_unlabel["Description"].fillna('') + " " + df_unlabel["Location"].fillna('') + " " + df_unlabel["Post"].fillna('') + " " + df_unlabel["Company"].fillna('')

stopWords = set(stopwords.words('french', 'english'))

# vectorize the post
vectorizer = TfidfVectorizer(stop_words=stopWords)

X = vectorizer.fit_transform(df_label['All'].values.astype('U'))
y = df_label["Annoted"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=3)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)

print("Accuracy:", score)

test = vectorizer.fit_transform(df_unlabel['All'].values.astype('U'))
classifier.predict(test)
