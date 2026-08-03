import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

df=pd.read_csv("C:\Users\HP\OneDrive\Desktop\Ai Workshop\Project\house_price_model.pkl.csv")
x=df[['Area','Bedrooms','Age']]
y=df['Price']

model=LinearRegression()
model.fit(x,y)

with open("house_price_model.pkl","wb") as file:
    pickle.dump(model,file)
print("Model saved successfully.")