import google.generativeai as genai
import pandas as pd

# setup
genai.configure(api_key="API_KEY_oonga boonga")
model = genai.GenerativeModel("gemini-1.5-flash")

# your classes
classes = ["Positive", "Negative", "Frustration", "Humor/Sarcasm", "Chill/Neutral"]

def classify_with_gemini(sentence):
    prompt = f"""
    Classify the following Gen-Z style sentence into one of these classes:
    {classes}.
    Only return the class name.

    Sentence: "{sentence}"
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# load dataset
df = pd.read_excel("Words.xlsx")  # must have 'sentence' column

# classify
df["gemini_label"] = df["sentence"].apply(classify_with_gemini)

df.to_excel("Words.xlsx", startrow= 1, startcol=3,index=False)
