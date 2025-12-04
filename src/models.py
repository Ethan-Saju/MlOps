from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier

models = [
    # RandomForestClassifier(),
    # LogisticRegression(),
    # SVC(probability=True),
    # DecisionTreeClassifier(),
    # GaussianNB(),
    KNeighborsClassifier(),
    GradientBoostingClassifier()
]