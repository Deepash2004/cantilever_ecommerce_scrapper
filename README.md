# cantilever_ecommerce_scrapper
readme_content = """# 🛒 E-commerce Scraper Project

This project demonstrates how to:
- Scrape data from an e-commerce website (BooksToScrape demo site).
- Store data in **Excel** and **SQLite database**.
- Visualize product trends using **Matplotlib** and **Seaborn**.
- Build a simple **Flask web app** with search functionality to explore the scraped data.

---

## 📂 Project Structure
ecommerce_scraper_project/
│── scraper.py # Scrape product data & save to Excel + SQLite
│── app.py # Flask web app with product search
│── visualize.py # Data visualization with Seaborn/Matplotlib
│── requirements.txt # Python dependencies
│── README.md # Documentation
│── templates/
└── index.html # Flask HTML template

yaml
Copy code

---

## 🚀 Getting Started

### 1️⃣ Clone or unzip the project
```bash
unzip ecommerce_scraper_project.zip
cd ecommerce_scraper_project
2️⃣ Install dependencies
If pip is available:

bash
Copy code
pip install -r requirements.txt
If pip is not available, use:

bash
Copy code
python -m pip install -r requirements.txt
🔍 Usage
🔹 Scrape products
bash
Copy code
python scraper.py
Scrapes product data from BooksToScrape.

Saves data into:

products.xlsx (Excel file)

products.db (SQLite database)

🔹 Visualize data
bash
Copy code
python visualize.py
Opens two plots:

Price distribution of products

Ratings count of products

🔹 Run the web app
bash
Copy code
python app.py
Opens a Flask server at http://127.0.0.1:5000/

Features:

Displays all scraped products

Search products by title
