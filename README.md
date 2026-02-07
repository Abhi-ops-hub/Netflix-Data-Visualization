# Netflix Data Analysis & Visualization 📊🎬

This project focuses on **exploratory data analysis (EDA)** and **data visualization** of Netflix content using **Python, Pandas, and Matplotlib**. The goal is to understand trends in Netflix movies and TV shows, including content distribution, ratings, durations, and release trends over the years.

---

## 📌 Project Objectives

* Analyze the distribution of **Movies vs TV Shows** on Netflix
* Visualize **content ratings** (TV-MA, TV-14, PG-13, etc.)
* Study **movie duration patterns**
* Compare **year-wise release trends** of Movies and TV Shows
* Practice real-world data cleaning and visualization techniques

---

## 🗂 Dataset

* **Source:** Netflix Titles Dataset
* **File:** `netflix_titles.csv`
* **Description:** Contains information about Netflix content such as title, type, director, cast, country, release year, rating, duration, and genre.

---

## 🛠️ Technologies Used

* **Python 3**
* **Pandas** – data loading and cleaning
* **Matplotlib** – data visualization
* **VS Code / Jupyter Notebook** – development environment

---

## 🔧 Data Cleaning Steps

* Removed rows with missing values in key columns like:

  * `type`
  * `rating`
  * `duration`
* Converted movie duration from text (e.g., `90 min`) to integer values
* Grouped and aggregated data for visualization

---

## 📊 Visualizations Created

### 1️⃣ Movies vs TV Shows (Bar Chart)

Shows the total number of movies and TV shows available on Netflix.

### 2️⃣ Content Ratings Distribution (Pie Chart)

Displays the percentage distribution of Netflix content ratings.

* Small categories grouped into **"Other"** for better readability

### 3️⃣ Movie Duration Distribution (Histogram)

Illustrates how movie durations are distributed across Netflix.

### 4️⃣ Movies vs TV Shows Over the Years (Line Charts)

Compares the number of movies and TV shows released each year.

---

## 📁 Project Structure

```
matplotlib/
│
├── projects/
│   ├── netflix_titles.csv
│   ├── sample_project.py
│   └── README.md
│
├── outputs/
│   ├── tv_shows_vs_movies.png
│   ├── content_ratings.png
│   ├── netflix_movie_duration.png
│   └── movies_vs_tv_shows_comparison.png
```

---

## ▶️ How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/netflix-data-analysis.git
   ```

2. Install required libraries:

   ```bash
   pip install pandas matplotlib
   ```

3. Run the Python script:

   ```bash
   python sample_project.py
   ```

4. Generated plots will be saved as `.png` files.

---

## 📈 Key Insights

* Netflix has **more movies than TV shows**, but TV shows have increased significantly in recent years.
* **TV-MA** and **TV-14** dominate Netflix’s content ratings.
* Most Netflix movies fall within the **80–120 minute** duration range.
* There is a noticeable growth in Netflix content after 2015.

---

## 🚀 Future Improvements

* Add interactive visualizations using **Seaborn or Plotly**
* Perform country-wise content analysis
* Analyze genre trends over time
* Integrate basic machine learning for content prediction

---

## 👤 Author

**Abhishek Goswami**
Aspiring Data Scientist & AI Engineer

---

⭐ If you find this project helpful, feel free to star the repository!
