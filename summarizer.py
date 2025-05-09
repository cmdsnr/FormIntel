from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_text(text):
    return summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']