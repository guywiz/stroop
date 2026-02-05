import pandas as pd
from scipy.stats import ttest_ind


df = pd.read_csv("memory_data.csv")


# Regrouper par position
mean_by_pos = df.groupby("position")["recalled"].mean()

print(mean_by_pos)


# Début vs fin
first = df[df["position"] <= 4]["recalled"]
last = df[df["position"] >= 9]["recalled"]


t, p = ttest_ind(last, first)

print("t =", t)
print("p =", p)

if p < 0.05:
    print("➡️ Effet de récence significatif")
else:
    print("➡️ Pas d'effet significatif")
