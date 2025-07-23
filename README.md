# 🛍️ Product Recommender System using Python

## ✅ Objective
This project builds a simple **item-based recommender system** using cosine similarity to recommend similar products based on user ratings. It is designed for beginner AI learners and submitted as part of the **YBI Foundation Internship**.

---

# Presented By : Gowthangaraj A
## Guided by : YBI Foundation
### 15 Days Internship 

## 📂 Dataset
A manually created dataset with user ratings for products:

| UserID | Product  | Rating |
|--------|----------|--------|
| U1     | Phone    | 5      |
| U1     | Laptop   | 4      |
| U2     | Phone    | 4      |
| U2     | Tablet   | 3      |
| U3     | Laptop   | 5      |
| U3     | Headset  | 4      |
| U4     | Phone    | 2      |
| U4     | Laptop   | 3      |

Saved as: `data_ratings.csv`

---

## 🛠️ Tools & Libraries Used
- Python 3.9+
- [Pandas](https://pandas.pydata.org/) for data handling
- [Scikit-learn](https://scikit-learn.org/) for cosine similarity
- [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)

---

## 🔍 How It Works

1. Load the product ratings dataset.
2. Encode categorical values using `LabelEncoder`.
3. Build a **user-item matrix** using pivot table.
4. Compute **cosine similarity** between products.
5. Recommend top N similar products.

---

## 📌 Sample Output

```text
Top 3 products similar to 'Phone':
- Laptop (Similarity Score: 0.91)
- Tablet (Similarity Score: 0.66)
- Headset (Similarity Score: 0.42)
