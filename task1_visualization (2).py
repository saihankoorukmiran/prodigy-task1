
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Histogram for Age Distribution
# -------------------------------

age_data = {
    "age": [18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50, 55, 60]
}

df_age = pd.DataFrame(age_data)

plt.figure(figsize=(8,5))
plt.hist(df_age["age"], bins=8)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.close()

# -------------------------------
# Bar Chart for Gender Distribution
# -------------------------------

gender_data = {
    "gender": ["Male", "Female", "Male", "Male", "Female", "Female", "Male"]
}

df_gender = pd.DataFrame(gender_data)

gender_counts = df_gender["gender"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")
plt.close()
