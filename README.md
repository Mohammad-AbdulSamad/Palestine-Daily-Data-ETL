# 🇵🇸 Palestine Daily Data ETL

[![Daily ETL](https://github.com/YOUR_USERNAME/palestine-daily-data-etl/actions/workflows/daily_etl.yml/badge.svg)](https://github.com/YOUR_USERNAME/palestine-daily-data-etl/actions/workflows/daily_etl.yml)

A fully automated ETL (Extract, Transform, Load) pipeline that fetches daily humanitarian data from [Tech For Palestine](https://data.techforpalestine.org/) APIs, transforms it into clean CSV files, and makes it ready for public visualization via Tableau Public.

---

## 🎯 Purpose

This project aims to **automate the collection and structuring of humanitarian data** from Gaza and the West Bank, enabling **transparent, real-time dashboards** that highlight:

- Civilian casualties  
- Journalist fatalities  
- Daily reports  
- Infrastructure damage  
- West Bank settler attacks  
- Summary statistics  

All data is saved in flat `.csv` format for easy public use and integration into visualization tools.

---

## 📦 Output

The pipeline produces the following datasets in the `data/` folder:

- `killed_in_gaza.csv`
- `press_killed_in_gaza.csv`
- `summary.csv`
- `daily_casualties_gaza.csv`
- `daily_casualties_west_bank.csv`
- `infrastructure_damaged.csv`

Each file includes a `fetched_at` column to track the last updated date.

---

## ⚙️ How It Works

This project uses **GitHub Actions** to run `etl.py` every day at 00:00 UTC.

1. Fetches live data from TechForPalestine APIs.
2. Parses and normalizes nested JSON structures.
3. Saves output to `/data` as CSV files.
4. Commits and pushes updated data back to the repository.

---

## 🗂️ Folder Structure

palestine-daily-data-etl/
  ├── data/ # Output CSV files (auto-updated)
  ├── etl.py # Main ETL script
  ├── requirements.txt # Python dependencies
  └── .github/
  └── workflows/
  └── daily_etl.yml # GitHub Actions workflow
---

## 📊 Visualization

To visualize the data in **Tableau Public**:

1. Sync this repo’s `data/` folder to **Google Drive** or **OneDrive** (e.g., using GitHub → Drive sync tools).
2. Connect Tableau Public to the synced CSVs.
3. Build dashboards and set them to auto-refresh from the cloud source.

---

## 🚀 Deployment Status

- ✅ Daily automation via GitHub Actions  
- ✅ Modular and extensible ETL structure  
- 🔜 Coming Soon: Google Drive sync for Tableau Public

---

## 🙌 Credits

Data provided by [Tech For Palestine](https://data.techforpalestine.org/).

Built by Mohammad Abdul-Samad, to raise awareness and increase access to transparent, up-to-date information.

---

## 🕊️ Free Palestine.
