import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Nom": ["Anouar", "Sara", "Karim", "Fatima", "Youssef", "Nadia", "Hassan", "Leila"],
    "Age": [28, 35, 42, 31, 55, 27, 48, 38],
    "Departement": ["IT", "RH", "IT", "Finance", "RH", "Finance", "IT", "RH"],
    "Salaire": [6000, 4500, 8500, 5200, 9000, 3800, 7500, 4800],
    "Annees_experience": [3, 8, 15, 6, 25, 2, 20, 10]
}

df = pd.DataFrame(data)

print("=== Aperçu des données ===")
print(df)
print("\n=== Description ===")
print(df.describe())
# 1 - Salaire par Département
df.groupby("Departement")["Salaire"].mean().plot(kind="bar", color=["steelblue","orange","green"])
plt.title("Salaire Moyen par Département")
plt.ylabel("Salaire")
plt.savefig("salaire_1_departement.png", bbox_inches="tight")
plt.show()

# 2 - Expérience vs Salaire
plt.figure()
plt.scatter(df["Annees_experience"], df["Salaire"], color="steelblue", s=100)
plt.title("Expérience vs Salaire")
plt.xlabel("Années d'expérience")
plt.ylabel("Salaire")
plt.grid(True)
plt.savefig("salaire_2_experience.png", bbox_inches="tight")
plt.show()

# 3 - Salaire par Employé
plt.figure()
plt.bar(df["Nom"], df["Salaire"], color="purple")
plt.title("Salaire par Employé")
plt.ylabel("Salaire")
plt.savefig("salaire_3_employe.png", bbox_inches="tight")
plt.show()

print("✅ Les 3 images sont sauvegardées !")
