
import os
import random
from supabase import create_client

supabase = None

# Create Supabase client, if not already created, reuse spares resources


def create_supabase_client():
    global supabase
    if not supabase:
        db_url: str = os.environ['SUPABASE_URL']
        db_key: str = os.environ['SUPABASE_KEY']
        supabase = create_client(db_url, db_key)
    return supabase

# Get random summary from Supabase


def get_random_summary():

    supabase = create_supabase_client()

    summary_ids = supabase.table('book_summaries').select(
        'id').execute()

    random_id = random.choice(summary_ids.data)['id']

    response = supabase.table('book_summaries').select(
        'id', 'title', 'summary', 'rating', 'author').eq('id', random_id).execute()

    # Separate quotes from the whole summary, and split into list of quotes
    quotes = response.data[0]['summary'].split('Lausahduksia:')[1].strip().split(
        '\n')
    # Remove empty strings, via list comprehension
    quotes = [i for i in quotes if i]

    formatted_quote = {
        'id': response.data[0]['id'],
        'title': response.data[0]['title'],
        'author': response.data[0]['author'],
        'rating': response.data[0]['rating'],
        'random_quote': random.choice(quotes)
    }

    return formatted_quote


if __name__ == "__main__":
    get_random_summary()
