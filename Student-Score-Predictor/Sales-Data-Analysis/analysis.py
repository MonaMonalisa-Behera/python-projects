import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["A", "B", "C", "D"],
    "Sales": [100, 200, 150, 300]
}

df = pd.DataFrame(data)

plt.bar(df["Product"], df["Sales"])
plt.title("Sales Data Analysis")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
