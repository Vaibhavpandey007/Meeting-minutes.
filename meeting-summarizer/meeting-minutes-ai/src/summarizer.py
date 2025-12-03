from transformers import pipeline
from .chunking import chunk_text

class MeetingMinutesGenerator:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)
        self.model_name = model_name

    def generate_minutes(self, text):
        # Chunk the text if it's too long
        chunks = chunk_text(text, model_name=self.model_name)
        
        summaries = []
        for chunk in chunks:
            # Generate summary for each chunk
            # Adjust max_length/min_length dynamically based on chunk size if needed
            summary = self.summarizer(chunk, max_length=150, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
            
        full_summary = " ".join(summaries)
        
        # If we have multiple chunks, we might want to summarize the summaries for the executive summary
        if len(chunks) > 1:
            executive_summary = self.summarizer(full_summary, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
        else:
            executive_summary = full_summary

        # For action items, we'll use a simple heuristic or a second pass if we had a specific model.
        # Since we only have a summarizer, we'll simulate it by asking for a bulleted list style summary 
        # or just returning the detailed summary as action items for now.
        # A better approach with a generic summarizer is hard without prompt engineering (which requires an LLM).
        # We will just use the full summary as the "Action Items" context for now, 
        # or perhaps try to extract sentences with "action" verbs if we want to be fancy.
        # For simplicity/robustness with this model:
        action_items = "• " + full_summary.replace(". ", ".\n• ")
        
        return {
            "executive_summary": executive_summary,
            "action_items": action_items
        }

def summarize_text(text):
    generator = MeetingMinutesGenerator()
    return generator.generate_minutes(text)
