# 🚢 Titanic Survival Analysis

## 📊 Project Overview

**Titanic Survival Analysis** is an Exploratory Data Analysis (EDA) project built using **Python, Pandas, NumPy, Matplotlib, and Seaborn**.

The objective of this project is to analyze the Titanic passenger dataset and identify the major factors associated with passenger survival.

The project uses an **Object-Oriented Programming (OOP)** approach and provides a **menu-driven interface**, allowing users to perform different analysis operations interactively.

The analysis focuses on factors such as:

* Passenger gender
* Passenger class
* Age
* Fare
* Overall survival
* Relationships between numerical variables
* Missing values

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Load and explore the Titanic dataset.
2. Understand the structure and basic information of the dataset.
3. Identify missing values.
4. Analyze the total number of survivors and non-survivors.
5. Compare survival between male and female passengers.
6. Analyze survival based on passenger class.
7. Analyze survival across different age groups.
8. Study fare distribution and its relationship with survival.
9. Calculate the overall survival percentage.
10. Analyze correlations between numerical variables.
11. Create meaningful data visualizations.
12. Generate business-style insights from the analysis.

---

## 🛠️ Technologies & Libraries

| Technology                     | Purpose                             |
| ------------------------------ | ----------------------------------- |
| **Python**                     | Programming language                |
| **Pandas**                     | Data manipulation and analysis      |
| **NumPy**                      | Numerical operations                |
| **Matplotlib**                 | Data visualization                  |
| **Seaborn**                    | Statistical visualization           |
| **Jupyter Notebook / VS Code** | Development environment             |
| **Git & GitHub**               | Version control and project sharing |

---

## 📁 Dataset

The project uses the **Titanic dataset**, which contains information about passengers who traveled on the RMS Titanic.

### Dataset Columns

| Column        | Description                                        |
| ------------- | -------------------------------------------------- |
| `survived`    | Survival status: 0 = Did not survive, 1 = Survived |
| `pclass`      | Passenger class: 1, 2, or 3                        |
| `sex`         | Passenger gender                                   |
| `age`         | Passenger age                                      |
| `sibsp`       | Number of siblings/spouses aboard                  |
| `parch`       | Number of parents/children aboard                  |
| `fare`        | Passenger ticket fare                              |
| `embarked`    | Port of embarkation                                |
| `class`       | Passenger class as a categorical value             |
| `who`         | Passenger category such as man, woman, or child    |
| `adult_male`  | Whether the passenger was an adult male            |
| `deck`        | Passenger deck                                     |
| `embark_town` | Name of embarkation town                           |
| `alive`       | Survival status as Yes/No                          |
| `alone`       | Whether the passenger traveled alone               |

---

## 📌 Project Structure

```text
Titanic-Survival-Analysis/
│
├── data/
│   └── titanic.csv
│
├── Titanic_Survival_Analysis.py
│
├── README.md
│
└── screenshots/
    ├── survival_count.png
    ├── survival_gender.png
    ├── survival_class.png
    ├── survival_age.png
    ├── fare_analysis.png
    ├── survival_percentage.png
    └── correlation_heatmap.png
```

---

# ⚙️ Project Features

The project provides a menu-driven system with the following operations:

```text
==========================================
       TITANIC SURVIVAL ANALYSIS
==========================================

1. Load Data
2. Basic Information
3. Check Missing Values
4. Survival Count
5. Survival by Gender
6. Survival by Passenger Class
7. Survival by Age
8. Fare Analysis
9. Survival Percentage
10. Correlation Analysis
11. Final Conclusion
12. Exit
==========================================
```

---

# 🔍 Analysis Performed

## 1. Load Data

The user provides the CSV file path, and the program loads the dataset using Pandas.

The program displays:

* First 5 rows
* Number of rows
* Number of columns

Example:

```python
df = pd.read_csv(file_path)
```

---

## 2. Basic Information

The project explores the basic structure of the dataset.

It displays:

* Dataset shape
* Column names
* Data types
* First five rows
* Statistical information

---

## 3. Missing Value Analysis

Missing values are identified using:

```python
df.isnull().sum()
```

A **Seaborn heatmap** is also created to visually identify missing values.

### Visualization

**Missing Values Heatmap**

This helps understand which columns contain incomplete passenger information.

---

## 4. Survival Count Analysis

The project calculates the number of passengers who:

* Survived
* Did not survive

The analysis uses:

```python
df["survived"].value_counts()
```

### Visualization

**Survival Count Plot**

The count plot makes it easy to compare survivors and non-survivors.

---

## 5. Survival by Gender

The project compares survival between:

* Male passengers
* Female passengers

A cross-tabulation is used to summarize the results.

### Visualization

**Survival by Gender Count Plot**

This helps identify differences in survival outcomes between genders.

---

## 6. Survival by Passenger Class

Passenger survival is analyzed across:

* First Class
* Second Class
* Third Class

### Visualization

**Survival by Passenger Class**

This analysis helps understand whether passenger class was associated with survival.

---

## 7. Survival by Age

Passengers are grouped into different age categories:

| Age Range | Group       |
| --------- | ----------- |
| 0–12      | Child       |
| 13–18     | Teenager    |
| 19–30     | Young Adult |
| 31–50     | Adult       |
| 51–100    | Senior      |

### Visualization

**Survival by Age Group**

This visualization allows comparison of survival across different age groups.

---

## 8. Fare Analysis

The project analyzes passenger ticket fares.

It calculates:

* Average fare
* Minimum fare
* Maximum fare
* Average fare by survival status

A box plot is used to visualize fare distribution.

### Visualization

**Fare Distribution by Survival**

This helps identify differences in fare distribution between passengers who survived and those who did not.

---

## 9. Survival Percentage

The project calculates:

* Total passengers
* Number of survivors
* Number of non-survivors
* Survival percentage
* Non-survival percentage

### Visualization

**Titanic Survival Percentage Pie Chart**

The pie chart provides a simple visual representation of the overall survival distribution.

---

## 10. Correlation Analysis

The project selects numerical columns and calculates their correlation.

Example numerical variables include:

* `survived`
* `pclass`
* `age`
* `sibsp`
* `parch`
* `fare`
* `adult_male`
* `alone`

### Visualization

**Correlation Heatmap**

The heatmap helps identify positive and negative relationships between numerical variables.

---

# 📈 Visualizations

The project uses the following visualizations:

### 1. Missing Values Heatmap

```text
Missing Values
      ↓
Seaborn Heatmap
      ↓
Identify incomplete columns
```

### 2. Survival Count

```text
Survived vs Not Survived
          ↓
      Count Plot
```

### 3. Survival by Gender

```text
Male vs Female
      ↓
Survival Comparison
      ↓
Count Plot
```

### 4. Survival by Passenger Class

```text
1st Class
2nd Class
3rd Class
    ↓
Survival Comparison
```

### 5. Survival by Age Group

```text
Child
Teenager
Young Adult
Adult
Senior
   ↓
Survival Comparison
```

### 6. Fare Analysis

```text
Fare Distribution
       ↓
    Box Plot
```

### 7. Survival Percentage

```text
Survived
    vs
Not Survived
    ↓
Pie Chart
```

### 8. Correlation Analysis

```text
Numerical Variables
        ↓
Correlation Matrix
        ↓
Heatmap
```

---

# 💡 Key Insights

The EDA provides several important observations:

### 👩 Gender

Female passengers generally had a higher survival rate compared with male passengers.

### 🚢 Passenger Class

Passengers in higher classes generally had better survival outcomes compared with passengers in lower classes.

### 👶 Age

Age was also associated with survival, with younger passengers showing different survival patterns from adults.

### 💰 Fare

Higher fares were generally associated with higher passenger classes, and fare distributions differed between survivors and non-survivors.

### 📊 Overall Survival

The Titanic dataset shows that the number of passengers who did not survive was greater than the number who survived.

> **Note:** These findings describe associations in the dataset and should not be interpreted as proof that a single factor directly caused survival.

---

# 🧠 OOP Implementation

The project is implemented using an Object-Oriented Programming approach.

The main class is:

```python
class TitanicAnalysis:
```

The class contains separate methods for each analysis operation.

Example:

```python
def survival_by_gender(self):
```

```python
def survival_by_class(self):
```

```python
def survival_by_age(self):
```

```python
def fare_analysis(self):
```

This structure makes the project:

* Organized
* Reusable
* Easy to understand
* Easy to modify
* Suitable for beginners learning OOP

---

# 🔄 Menu-Driven System

The project uses a menu-driven approach so the user can select an operation.

Example:

```text
Enter your choice (1-12): 5
```

The program then executes:

```python
self.survival_by_gender()
```

This allows users to perform individual analyses without running the entire project again.

---

# 💻 Installation

## Step 1: Install Python

Install Python 3.x on your system.

Verify the installation:

```bash
python --version
```

---

## Step 2: Install Required Libraries

Run:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## Step 3: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd Titanic-Survival-Analysis
```

---

# ▶️ How to Run

Run the Python program:

```bash
python Titanic_Survival_Analysis.py
```

Then enter the path of your Titanic CSV file.

Example:

```text
Enter Titanic CSV file path: data/titanic.csv
```

After loading the dataset, select an operation from the menu.

---

# 📊 Sample Workflow

```text
1. Load Data
        ↓
2. Basic Information
        ↓
3. Check Missing Values
        ↓
4. Survival Count
        ↓
5. Survival by Gender
        ↓
6. Survival by Passenger Class
        ↓
7. Survival by Age
        ↓
8. Fare Analysis
        ↓
9. Survival Percentage
        ↓
10. Correlation Analysis
        ↓
11. Final Conclusion
```

---

# 🎓 Skills Demonstrated

This project demonstrates the following skills:

### Python

* Variables
* Conditional statements
* Loops
* Functions
* Classes and objects
* Exception handling
* User input

### Pandas

* CSV data loading
* DataFrame operations
* Filtering
* GroupBy
* Cross-tabulation
* Missing-value analysis
* Statistical analysis

### NumPy

* Numerical operations
* Numeric column selection
* Correlation-related calculations

### Matplotlib

* Pie charts
* Figure customization
* Titles
* Axis labels

### Seaborn

* Count plots
* Box plots
* Heatmaps
* Statistical visualizations

### Data Analysis

* Exploratory Data Analysis
* Data cleaning awareness
* Univariate analysis
* Bivariate analysis
* Correlation analysis
* Data visualization
* Insight generation

---

# 🚀 Future Improvements

The project can be extended with:

* Interactive dashboards using Power BI or Tableau
* More advanced age analysis
* Survival rate by embarkation town
* Survival analysis based on family size
* Survival analysis based on `sibsp` and `parch`
* Fare vs age analysis
* Passenger class vs fare analysis
* Interactive Plotly charts
* Automated data cleaning
* Machine Learning survival prediction
* Streamlit web application
* Export analysis results to Excel

---

# 📌 Conclusion

The **Titanic Survival Analysis** project demonstrates how Python can be used to perform Exploratory Data Analysis on a real-world dataset.

By analyzing passenger characteristics such as **gender, passenger class, age, and fare**, the project identifies patterns associated with survival.

The project also demonstrates practical use of:

**Python + Pandas + NumPy + Matplotlib + Seaborn + OOP + Data Visualization**

This project is suitable as a **beginner-to-intermediate Data Analyst portfolio project** and demonstrates fundamental skills required for working with structured datasets.

---

## 👨‍💻 Author

**Dharmendra Rajput**

**Aspiring Data Analyst**

Skills:

`Python` • `Pandas` • `NumPy` • `SQL` • `Matplotlib` • `Seaborn` • `Data Analysis` • `Data Visualization`

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
