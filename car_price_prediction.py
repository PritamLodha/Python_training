import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# sample data
data = {
    "year": [2015, 2016, 2017, 2018, 2019],
    "mileage": [50000, 40000, 35000, 30000, 20000],
    "brand": ["Toyota", "Honda", "Honda", "Toyota", "BMW"],
    "price": [700000, 800000, 850000, 900000, 1500000]
}

df = pd.DataFrame(data)

# convert brand into numeric
df = pd.get_dummies(df, columns=["brand"])

# features and target
X = df.drop("price", axis=1)
y = df["price"]

# split data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
model = LinearRegression()
model.fit(x_train, y_train)

# test prediction
pred = model.predict(x_test)
print("Predicted values:", pred)
print("Actual values:", list(y_test))

# check error
mse = mean_squared_error(y_test, pred)
print("MSE:", mse)

# -------------------------------
# predict new car price
# -------------------------------

# example new data as raw values
new_car = pd.DataFrame([
    {"year": 2020, "mileage": 10000, "brand": "BMW"}
])

# encode the new sample using the same dummy columns as the training data
new_car_encoded = pd.get_dummies(new_car, columns=["brand"])
new_car_encoded = new_car_encoded.reindex(columns=X.columns, fill_value=0)

result = model.predict(new_car_encoded)
print("Estimated price:", result[0])