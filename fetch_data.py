
import os
import random
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

db_url: str = os.getenv('SUPABASE_URL')
db_key: str = os.getenv('SUPABASE_KEY')

supabase: Client = create_client(db_url, db_key)


summary_ids = supabase.table('book_summaries').select(
    'id').execute()

random_id = random.choice(summary_ids.data)['id']

response = supabase.table('book_summaries').select(
    'id', 'title', 'summary', 'rating', 'author').eq('id', random_id).execute()

print("Randomly picked ID: ", random_id)
print("Title: ", response.data[0]['title'])
print("Author: ", response.data[0]['author'])
print("Rating: ", response.data[0]['rating'], "/ 5")
# print("Summary: ", response.data[0]['summary'])
