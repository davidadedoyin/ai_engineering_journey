import matplotlib  # type: ignore[reportMissingModuleSource]
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]
import seaborn as sns  # type: ignore[reportMissingModuleSource]


def main():
    df = sns.load_dataset("titanic")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("Missing values:")
    print(df.isnull().sum().to_string())

    print("Age summary:")
    print(df["age"].describe())

    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"].dropna(), bins=20, kde=True)
    plt.title("Age distribution on Titanic")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("titanic_age_distribution.png")
    print("Saved chart: titanic_age_distribution.png")


if __name__ == "__main__":
    main()
