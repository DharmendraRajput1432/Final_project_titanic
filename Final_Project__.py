# ============================================================
# TITANIC SURVIVAL ANALYSIS
# EDA PROJECT USING OOP + MENU DRIVEN PROGRAM
# ============================================================

# ---------------- IMPORT LIBRARIES ----------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CLASS: TitanicAnalysis
# ============================================================

class TitanicAnalysis:

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------

    def __init__(self):
        self.df = None

        print("\n==========================================")
        print("     TITANIC SURVIVAL ANALYSIS")
        print("==========================================")


    # ========================================================
    # 1. LOAD DATA
    # ========================================================

    def load_data(self):

        file_path = input("\nEnter Titanic CSV file path: ")

        try:

            self.df = pd.read_csv(file_path)

            print("\nData Loaded Successfully!")

            print("\nFirst 5 Rows:")
            print(self.df.head())

            print("\nDataset Shape:")
            print(self.df.shape)

        except FileNotFoundError:

            print("\nFile Not Found!")
            print("Please check your CSV file path.")

        except Exception as e:

            print("\nError:", e)


    # ========================================================
    # 2. BASIC INFORMATION
    # ========================================================

    def basic_information(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("          BASIC INFORMATION")
        print("==========================================")

        print("\nDataset Shape:")
        print(self.df.shape)

        print("\nColumn Names:")
        print(self.df.columns.tolist())

        print("\nData Types:")
        print(self.df.dtypes)

        print("\nFirst 5 Rows:")
        print(self.df.head())

        print("\nStatistical Information:")
        print(self.df.describe(include="all"))


    # ========================================================
    # 3. CHECK MISSING VALUES
    # ========================================================

    def missing_values(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("          MISSING VALUES")
        print("==========================================")

        missing = self.df.isnull().sum()

        print(missing)

        print("\nTotal Missing Values:",
              self.df.isnull().sum().sum())

        # Visualization

        plt.figure(figsize=(10, 5))

        sns.heatmap(
            self.df.isnull(),
            cbar=False
        )

        plt.title("Missing Values in Titanic Dataset")
        plt.xlabel("Columns")
        plt.ylabel("Rows")

        plt.show()


    # ========================================================
    # 4. SURVIVAL COUNT
    # ========================================================

    def survival_count(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("            SURVIVAL COUNT")
        print("==========================================")

        print("\nSurvival Count:")

        print(
            self.df["survived"].value_counts()
        )

        # Visualization

        plt.figure(figsize=(7, 5))

        sns.countplot(
            data=self.df,
            x="survived"
        )

        plt.title("Titanic Survival Count")
        plt.xlabel("Survived (0 = No, 1 = Yes)")
        plt.ylabel("Number of Passengers")

        plt.show()


    # ========================================================
    # 5. SURVIVAL BY GENDER
    # ========================================================

    def survival_by_gender(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("          SURVIVAL BY GENDER")
        print("==========================================")

        result = pd.crosstab(
            self.df["sex"],
            self.df["survived"]
        )

        print(result)

        # Visualization

        plt.figure(figsize=(7, 5))

        sns.countplot(
            data=self.df,
            x="sex",
            hue="survived"
        )

        plt.title("Survival by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Number of Passengers")

        plt.legend(
            title="Survived",
            labels=["No", "Yes"]
        )

        plt.show()


    # ========================================================
    # 6. SURVIVAL BY PASSENGER CLASS
    # ========================================================

    def survival_by_class(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("       SURVIVAL BY PASSENGER CLASS")
        print("==========================================")

        result = pd.crosstab(
            self.df["pclass"],
            self.df["survived"]
        )

        print(result)

        # Visualization

        plt.figure(figsize=(7, 5))

        sns.countplot(
            data=self.df,
            x="pclass",
            hue="survived"
        )

        plt.title("Survival by Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Number of Passengers")

        plt.legend(
            title="Survived",
            labels=["No", "Yes"]
        )

        plt.show()


    # ========================================================
    # 7. SURVIVAL BY AGE
    # ========================================================

    def survival_by_age(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("             SURVIVAL BY AGE")
        print("==========================================")

        # Create age groups

        self.df["age_group"] = pd.cut(
            self.df["age"],
            bins=[0, 12, 18, 30, 50, 100],
            labels=[
                "Child",
                "Teenager",
                "Young Adult",
                "Adult",
                "Senior"
            ]
        )

        print("\nAge Group Survival:")

        result = pd.crosstab(
            self.df["age_group"],
            self.df["survived"]
        )

        print(result)

        # Visualization

        plt.figure(figsize=(9, 5))

        sns.countplot(
            data=self.df,
            x="age_group",
            hue="survived"
        )

        plt.title("Survival by Age Group")
        plt.xlabel("Age Group")
        plt.ylabel("Number of Passengers")

        plt.xticks(rotation=20)

        plt.legend(
            title="Survived",
            labels=["No", "Yes"]
        )

        plt.show()


    # ========================================================
    # 8. FARE ANALYSIS
    # ========================================================

    def fare_analysis(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("              FARE ANALYSIS")
        print("==========================================")

        print("\nAverage Fare:")

        print(
            self.df["fare"].mean()
        )

        print("\nMinimum Fare:")

        print(
            self.df["fare"].min()
        )

        print("\nMaximum Fare:")

        print(
            self.df["fare"].max()
        )

        print("\nAverage Fare by Survival:")

        print(
            self.df.groupby("survived")["fare"].mean()
        )

        # Visualization

        plt.figure(figsize=(8, 5))

        sns.boxplot(
            data=self.df,
            x="survived",
            y="fare"
        )

        plt.title("Fare Distribution by Survival")
        plt.xlabel("Survived (0 = No, 1 = Yes)")
        plt.ylabel("Fare")

        plt.show()


    # ========================================================
    # 9. SURVIVAL PERCENTAGE
    # ========================================================

    def survival_percentage(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("          SURVIVAL PERCENTAGE")
        print("==========================================")

        total_passengers = len(self.df)

        survived = self.df["survived"].sum()

        not_survived = total_passengers - survived

        survived_percentage = (
            survived / total_passengers
        ) * 100

        not_survived_percentage = (
            not_survived / total_passengers
        ) * 100

        print(
            "\nTotal Passengers:",
            total_passengers
        )

        print(
            "Survived:",
            survived
        )

        print(
            "Not Survived:",
            not_survived
        )

        print(
            "\nSurvival Percentage:",
            round(survived_percentage, 2),
            "%"
        )

        print(
            "Non-Survival Percentage:",
            round(not_survived_percentage, 2),
            "%"
        )

        # Visualization

        labels = ["Survived", "Not Survived"]

        values = [
            survived,
            not_survived
        ]

        plt.figure(figsize=(7, 7))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Titanic Survival Percentage")

        plt.show()


    # ========================================================
    # 10. CORRELATION ANALYSIS
    # ========================================================

    def correlation_analysis(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("          CORRELATION ANALYSIS")
        print("==========================================")

        # Select numeric columns

        numeric_data = self.df.select_dtypes(
            include=np.number
        )

        correlation = numeric_data.corr()

        print("\nCorrelation Matrix:")

        print(correlation)

        # Visualization

        plt.figure(figsize=(10, 7))

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title("Titanic Numeric Correlation Heatmap")

        plt.show()


    # ========================================================
    # 11. FINAL CONCLUSION
    # ========================================================

    def final_conclusion(self):

        if self.df is None:

            print("\nPlease load the data first.")
            return

        print("\n==========================================")
        print("             FINAL CONCLUSION")
        print("==========================================")

        print(
            "\n1. Gender had a strong influence on survival."
        )

        print(
            "   Female passengers generally had a higher"
            " survival rate than male passengers."
        )

        print(
            "\n2. Passenger class influenced survival."
        )

        print(
            "   First-class passengers generally had better"
            " survival chances than lower classes."
        )

        print(
            "\n3. Age also influenced survival."
        )

        print(
            "   Children received relatively better chances"
            " of survival compared with some adult groups."
        )

        print(
            "\n4. Fare was related to passenger class."
        )

        print(
            "   Passengers paying higher fares were often"
            " traveling in higher passenger classes."
        )

        print(
            "\n5. Overall survival was lower than the"
            " number of passengers who did not survive."
        )

        print(
            "\nConclusion:"
        )

        print(
            "Gender, passenger class, age and fare were"
            " important factors associated with Titanic"
            " passenger survival."
        )


    # ========================================================
    # 12. MENU DRIVEN PROGRAM
    # ========================================================

    def menu(self):

        while True:

            print("\n")
            print("==========================================")
            print("       TITANIC SURVIVAL ANALYSIS")
            print("==========================================")

            print("1. Load Data")
            print("2. Basic Information")
            print("3. Check Missing Values")
            print("4. Survival Count")
            print("5. Survival by Gender")
            print("6. Survival by Passenger Class")
            print("7. Survival by Age")
            print("8. Fare Analysis")
            print("9. Survival Percentage")
            print("10. Correlation Analysis")
            print("11. Final Conclusion")
            print("12. Exit")

            print("==========================================")

            choice = input(
                "\nEnter your choice (1-12): "
            )

            if choice == "1":

                self.load_data()

            elif choice == "2":

                self.basic_information()

            elif choice == "3":

                self.missing_values()

            elif choice == "4":

                self.survival_count()

            elif choice == "5":

                self.survival_by_gender()

            elif choice == "6":

                self.survival_by_class()

            elif choice == "7":

                self.survival_by_age()

            elif choice == "8":

                self.fare_analysis()

            elif choice == "9":

                self.survival_percentage()

            elif choice == "10":

                self.correlation_analysis()

            elif choice == "11":

                self.final_conclusion()

            elif choice == "12":

                print(
                    "\nThank you for using "
                    "Titanic Survival Analysis!"
                )

                break

            else:

                print(
                    "\nInvalid choice!"
                    " Please enter 1-12."
                )


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    obj = TitanicAnalysis()

    obj.menu()