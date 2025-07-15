import requests
import pandas as pd
from datetime import date
import os

from sqlalchemy import create_engine
import pandas as pd
import requests
from datetime import date
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# === Output Directory ===
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


# === Correct API URLs ===
API_URLS = {
    "killed_in_gaza": "https://data.techforpalestine.org/api/v2/killed-in-gaza.json",
    "press_killed": "https://data.techforpalestine.org/api/v2/press_killed_in_gaza.json",
    "summary": "https://data.techforpalestine.org/api/v3/summary.json",
    "daily_casualties_gaza": "https://data.techforpalestine.org/api/v2/casualties_daily.json",
    "daily_casualties_west_bank": "https://data.techforpalestine.org/api/v2/west_bank_daily.json",
    "infrastructure_damaged": "https://data.techforpalestine.org/api/v3/infrastructure-damaged.json"
}





def fetch_json(endpoint: str):
    print(f"📥 Fetching: {endpoint}")
    res = requests.get(endpoint)
    res.raise_for_status()
    return res.json()





# === Fetch & Store Function ===
def store(data, name):
    try:
        # Flatten if "data" key exists
        if isinstance(data, dict) and "data" in data:
            data = data["data"]

        df = pd.json_normalize(data)
        df["fetched_at"] = date.today().isoformat()

        output_path = os.path.join(DATA_DIR, f"{name}.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"❌ Failed to fetch {name}: {e}")




ETL_PIPELINES = {
    "killed_in_gaza": {
        "url": API_URLS["killed_in_gaza"],
        # "transform": transform_killed_in_gaza,
        "table": "killed_in_gaza"
    },
    "press_killed": {
        "url": API_URLS["press_killed"],
        # "transform": transform_press_killed,
        "table": "press_killed_in_gaza"
    },
    "summary": {
        "url": API_URLS["summary"],
        # "transform": transform_summary,
        "table": "summary"
    },
    "daily_casualties_gaza": {
        "url": API_URLS["daily_casualties_gaza"],
        # "transform": transform_daily_casualties_gaza,
        "table": "daily_casualties_gaza"
    },
    "daily_casualties_west_bank": {
        "url": API_URLS["daily_casualties_west_bank"],
        # "transform": transform_daily_casualties_west_bank,
        "table": "daily_casualties_west_bank"
    },
    "infrastructure_damaged": {
        "url": API_URLS["infrastructure_damaged"],
        # "transform": transform_infrastructure_damaged,
        "table": "infrastructure_damaged"
    }
}

def run_all_etl():
    for name, config in ETL_PIPELINES.items():
        print(f"🚀 Running ETL for {name}")
        data = fetch_json(config["url"])
        # df = config["transform"](data)
        file_name = config["table"]
        store(data,file_name)

        # --For supabase db -- #
        # load_to_supabase(df, file_name)


# === Main Execution ===
if __name__ == "__main__":
    run_all_etl()
    # for name, url in API_URLS.items():
    #     fetch_and_store(name, url)

    #
    # def transform_killed_in_gaza(data):
    #     df = pd.DataFrame(data)
    #     df["fetched_at"] = date.today()
    #     return df
    #
    #
    # def transform_press_killed(data):
    #     df = pd.DataFrame(data)
    #     df["fetched_at"] = date.today()
    #     return df
    #
    #
    # def transform_summary(data):
    #     s = data
    #
    #     row = {
    #         "report_date": s.get("last_update"),
    #         # or set report date from 'gaza' or 'west_bank' last_update if you prefer
    #         # Gaza statistics
    #         "gaza_reports": s["gaza"].get("reports"),
    #         "gaza_massacres": s["gaza"].get("massacres"),
    #         "gaza_killed_total": s["gaza"]["killed"].get("total"),
    #         "gaza_killed_children": s["gaza"]["killed"].get("children"),
    #         "gaza_killed_women": s["gaza"]["killed"].get("women"),
    #         "gaza_killed_civil_defence": s["gaza"]["killed"].get("civil_defence"),
    #         "gaza_killed_press": s["gaza"]["killed"].get("press"),
    #         "gaza_killed_medical": s["gaza"]["killed"].get("medical"),
    #         "gaza_injured_total": s["gaza"]["injured"].get("total"),
    #
    #         # West Bank statistics
    #         "west_bank_reports": s["west_bank"].get("reports"),
    #         "west_bank_settler_attacks": s["west_bank"].get("settler_attacks"),
    #         "west_bank_killed_total": s["west_bank"]["killed"].get("total"),
    #         "west_bank_killed_children": s["west_bank"]["killed"].get("children"),
    #         "west_bank_injured_total": s["west_bank"]["injured"].get("total"),
    #         "west_bank_injured_children": s["west_bank"]["injured"].get("children"),
    #
    #         # Known killed in Gaza (by gender and age)
    #         "known_killed_records": s["known_killed_in_gaza"].get("records"),
    #         "male_adult": s["known_killed_in_gaza"]["male"].get("adult"),
    #         "male_senior": s["known_killed_in_gaza"]["male"].get("senior"),
    #         "male_child": s["known_killed_in_gaza"]["male"].get("child"),
    #         "female_adult": s["known_killed_in_gaza"]["female"].get("adult"),
    #         "female_senior": s["known_killed_in_gaza"]["female"].get("senior"),
    #         "female_child": s["known_killed_in_gaza"]["female"].get("child"),
    #
    #         # Known press killed in Gaza
    #         "known_press_killed_records": s["known_press_killed_in_gaza"].get("records")
    #     }
    #
    #     return pd.DataFrame([row])
    #
    #
    # def transform_daily_casualties_gaza(data):
    #     df = pd.json_normalize(data)
    #     df['fetched_at'] = date.today()
    #     return df
    #
    #
    # def transform_daily_casualties_west_bank(data):
    #     rows = []
    #
    #     for item in data:
    #         row = {
    #             "report_date": item["report_date"],
    #             "flash_source": item.get("flash_source"),
    #             "killed_cum": item.get("killed_cum"),
    #             "injured_cum": item.get("injured_cum"),
    #             "killed_children_cum": item.get("killed_children_cum"),
    #             "injured_children_cum": item.get("injured_children_cum"),
    #             "settler_attacks_cum": item.get("settler_attacks_cum"),
    #             "fetched_at": date.today()
    #         }
    #
    #         verified = item.get("verified", {})
    #         for field in ["killed", "killed_cum", "injured", "injured_cum",
    #                       "killed_children", "killed_children_cum",
    #                       "injured_children", "injured_children_cum"]:
    #             row[f"verified_{field}"] = verified.get(field)
    #
    #         rows.append(row)
    #
    #     return pd.DataFrame(rows)
    #
    #
    # def transform_infrastructure_damaged(data):
    #     rows = []
    #
    #     for item in data:
    #         row = {"report_date": item["report_date"]}
    #
    #         civic = item.get("civic_buildings", {})
    #         row["civic_buildings_destroyed"] = civic.get("destroyed")
    #         row["civic_buildings_ext_destroyed"] = civic.get("ext_destroyed")
    #
    #         edu = item.get("educational_buildings", {})
    #         row["educational_buildings_destroyed"] = edu.get("destroyed")
    #         row["educational_buildings_ext_destroyed"] = edu.get("ext_destroyed")
    #         row["educational_buildings_damaged"] = edu.get("damaged")
    #         row["educational_buildings_ext_damaged"] = edu.get("ext_damaged")
    #
    #         worship = item.get("places_of_worship", {})
    #         row["places_of_worship_mosques_destroyed"] = worship.get("mosques_destroyed")
    #         row["places_of_worship_ext_mosques_destroyed"] = worship.get("ext_mosques_destroyed")
    #         row["places_of_worship_mosques_damaged"] = worship.get("mosques_damaged")
    #         row["places_of_worship_ext_mosques_damaged"] = worship.get("ext_mosques_damaged")
    #         row["places_of_worship_churches_destroyed"] = worship.get("churches_destroyed")
    #         row["places_of_worship_ext_churches_destroyed"] = worship.get("ext_churches_destroyed")
    #
    #         residential = item.get("residential", {})
    #         row["residential_destroyed"] = residential.get("destroyed")
    #         row["residential_ext_destroyed"] = residential.get("ext_destroyed")
    #
    #         rows.append(row)
    #
    #     return pd.DataFrame(rows)
    #
    #
    # def load_to_supabase(df, table_name):
    #     engine = get_engine()
    #     with engine.begin() as conn:
    #         df.to_sql(table_name, conn, if_exists='append', index=False, method='multi')
    #     print(f"✅ Loaded {len(df)} rows into {table_name}")

#     # Supabase PostgreSQL credentials
# DB_CONFIG = {
#     "host": os.getenv("SUPABASE_HOST"),
#     "port": os.getenv("SUPABASE_PORT"),
#     "database": os.getenv("SUPABASE_DATABASE"),
#     "user": os.getenv("SUPABASE_USER"),
#     "password": os.getenv("SUPABASE_PASSWORD")
# }
#
#
# def get_engine():
#     DATABASE_URL = f"postgresql://postgres.vdwpvymeisjvktxthblc:{DB_CONFIG['password']}@aws-0-eu-north-1.pooler.supabase.com:6543/postgres"
#     # DATABASE_URL = f"postgresql://postgres:{DB_CONFIG['password']}@db.vdwpvymeisjvktxthblc.supabase.co:5432/postgres"
#     return create_engine(DATABASE_URL)
#     # return create_engine(
#     #     f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
#     # )
#

