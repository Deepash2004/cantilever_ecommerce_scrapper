import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

def visualize():
    conn = sqlite3.connect("products.db")
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()

    # Clean price column
    df["Price"] = df["Price"].str.replace("£", "").astype(float)

    # Plot price distribution
    sns.histplot(df["Price"], bins=20, kde=True)
    plt.title("Price Distribution of Products")
    plt.show()

    # Ratings count
    sns.countplot(x="Rating", data=df)
    plt.title("Product Ratings Count")
    plt.show()

if __name__ == "__main__":
    visualize()
