import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "hours": [1,2,3,4,5],
    "score": [35,50,65,70,90]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["score"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[6]])

print("Predicted Score:", prediction)
