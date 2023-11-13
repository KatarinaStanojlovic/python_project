from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('blackjack_data.csv')
# Assuming you have loaded and prepared your dataset in df

# Define features and target variable
X = df[['Player\'s Hand', 'Dealer\'s Hand']]
y = df['Player Decision']

# Build the decision tree model
clf = DecisionTreeClassifier()
clf.fit(X, y)


from sklearn.tree import export_text

tree_rules = export_text(clf, feature_names=list(X.columns))
print(tree_rules)