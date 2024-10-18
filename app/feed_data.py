import pandas as pd
from db.models.text import Text
import uuid
from db.client import db

df = pd.read_csv('data/data.csv')

for _, row in df.iterrows():
    
    text_instance = Text(id = str(uuid.uuid4()), 
                            text=row['text']
                            )
    db.add(text_instance)
    db.commit()

print(f'Done inserting {len(df)} instances')
db.close()
