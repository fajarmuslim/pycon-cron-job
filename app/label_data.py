import time
import requests
import schedule
import pandas as pd
from db.client import engine
from db.models.label import Label
from db.client import db
from sqlalchemy.dialects.postgresql import insert


def get_label(text:str, label:str):
    api_url = f"http://0.0.0.0:8001/{label}/single"
    response = requests.post(api_url, 
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             json={'text': text})
    if response.status_code == 200:
        return response.json().get(f"{label}")
    else:
        return None


def job():
    text_table = pd.read_sql_table('text', engine.connect())
    label_table = pd.read_sql_table('label', engine.connect())


    # Get the ids in X that are not in Y
    unlabeled_data = text_table[~text_table['id'].isin(label_table['id'])]

    for idx, row in unlabeled_data.iterrows():
        sentiment = get_label(text=row['text'], label='sentiment')
        emotion = get_label(text=row['text'], label='emotion')

        stmt = insert(Label).values(
            id=row['id'], 
            sentiment=sentiment, 
            emotion=emotion
        ).on_conflict_do_nothing(index_elements=['id'])  # Skip insert if `id` already exists

        db.execute(stmt)
        # db.add(data_instance)
        db.commit()


    print(f"Done inserting {idx+1} instances")
    db.close()

schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)