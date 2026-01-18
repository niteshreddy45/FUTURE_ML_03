import pandas as pd
import re

# --- SETTINGS ---
INPUT_FILE = "twcs.csv"
OUTPUT_FILE = "kaggle_final_upload.csv"
SAMPLE_SIZE = 2000  # Let's take 2,000 clean pairs (enough for credit, small enough to upload)

print("⏳ Processing Twitter data...")

# 1. Load data
try:
    df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print(f"❌ Error: Could not find '{INPUT_FILE}'. Make sure it is in this folder!")
    exit()

# 2. Separate Questions and Answers
questions = df[df['inbound'] == True]
answers = df[df['inbound'] == False]

# 3. Merge them
merged = pd.merge(questions, answers, left_on='tweet_id', right_on='in_response_to_tweet_id', suffixes=('_q', '_a'))

# 4. Filter for simple Q&A pairs (Question and Answer)
final_df = merged[['text_q', 'text_a']].copy()
final_df.columns = ['Question', 'Answer']

# --- THE FIX: Aggressive Cleaning Function ---
def clean_text(text):
    text = str(text)
    # Remove @mentions (like @AppleSupport)
    text = re.sub(r'@\w+', '', text)
    # Remove URL links
    text = re.sub(r'http\S+', '', text)
    # Remove Newlines (Crucial! Newlines break CSV uploads)
    text = text.replace('\n', ' ').replace('\r', '')
    # Remove weird characters/emojis (Keep only standard text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove extra spaces
    text = text.strip()
    return text

print("🧹 Scrubbing data (removing emojis, links, and weird symbols)...")
final_df['Question'] = final_df['Question'].apply(clean_text)
final_df['Answer'] = final_df['Answer'].apply(clean_text)

# Remove empty rows after cleaning
final_df = final_df[final_df['Question'] != ""]
final_df = final_df[final_df['Answer'] != ""]

# Take the top sample
final_df = final_df.head(SAMPLE_SIZE)

# 5. Save
final_df.to_csv(OUTPUT_FILE, index=False)

print(f"🎉 Success! Created '{OUTPUT_FILE}' with {len(final_df)} clean rows.")
print("👉 Go upload this specific file to Dialogflow now.")