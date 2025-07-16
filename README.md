# 🇵🇸 Palestine Daily Data ETL & Live Dashboard

> **Real-time humanitarian tracking using public data, GitHub Actions, and Tableau**

---

## 📊 Project Overview

This project automatically fetches **daily humanitarian data** from [TechForPalestine](https://data.techforpalestine.org) APIs, processes it, and updates live datasets and charts.

It is designed to raise awareness and provide real-time visibility into the situation in **Gaza and the West Bank**, showcasing:

* Civilian casualties
* Press victims
* Infrastructure damage
* Summary statistics and trends

---

## ⚙️ Tech Stack

| Layer            | Tool/Service            | Purpose                          |
| ---------------- | ----------------------- | -------------------------------- |
| Data Source      | TechForPalestine API    | Live humanitarian data           |
| ETL + Automation | Python + GitHub Actions | Daily fetch + transform + upload |
| Storage          | Google Drive            | Synced CSVs for Tableau          |
| Visualization    | Tableau Public          | Dashboards and charts            |
| Deployment       | Tableau Public (hosted) | Shared public access             |

---

## 🚀 Live Dashboard

> 🌐 **[Click here to view the public Tableau dashboard](https://public.tableau.com/app/profile/your-username/viz/PalestineCasualtiesTracker/MainDashboard)**
> *(Auto-refreshes with updated Google Drive CSVs daily)*

---

## 📑 How It Works

1. **ETL script (`etl.py`)** fetches JSON from 6 endpoints
2. Normalizes + stores each as a `.csv` file in `/data`
3. GitHub Actions runs this every 24 hours
4. Updated CSVs are committed + pushed to GitHub
5. Then uploaded to a shared Google Drive folder
6. Tableau Public dashboard is connected to these Google Drive CSVs
7. Dashboard refreshes automatically with new data

---

## 🛠️ Setup Instructions

### Clone & Run ETL Locally

```bash
git clone https://github.com/Mohammad-AbdulSamad/Palestine-Daily-Data-ETL.git
cd Palestine-Daily-Data-ETL
pip install -r requirements.txt
python etl.py
```

### GitHub Actions Automation

* Daily cron job: runs ETL + uploads fresh CSVs
* `.github/workflows/daily_etl.yml`

### Google Drive Integration

* Uses a Google service account
* Uploads/replaces CSVs in a shared folder
* Credentials and folder ID are stored as GitHub secrets

---

## 📊 Sample Visualizations

* Time series: daily killed/injured in Gaza & West Bank
* Map view: geographic spread of casualties
* Pie/bar charts: gender/age breakdown, press/civil defense victims
* Trend: infrastructure damage by type (schools, mosques, homes)

---

## 🎨 Screenshots

![dashboard-preview](assets/dashboard_screenshot.png)

---

## 🌟 Why This Project Matters

* Real-world impact: visualizing injustice with real-time data
* Great portfolio piece: automation, ETL, APIs, dashboarding
* Clean, reproducible, and open-source pipeline

---

## 🚩 Future Improvements

* Add database support (e.g., Supabase) for analysis
* Host the dashboard on a personal website (embed iframe)
* Add email/Slack notifications when data updates
* Expand to other humanitarian datasets

---

## 📚 Credits

* Data Source: [TechForPalestine](https://data.techforpalestine.org)
* Dev: Mohammad Abdul-Samad

---

## 🌐 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📅 Daily Automation Status

[![Daily ETL](https://github.com/Mohammad-AbdulSamad/Palestine-Daily-Data-ETL/actions/workflows/daily_etl.yml/badge.svg)](https://github.com/Mohammad-AbdulSamad/Palestine-Daily-Data-ETL/actions/workflows/daily_etl.yml)

---

Feel free to fork, star, or contribute ✨
