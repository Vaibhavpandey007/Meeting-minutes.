from transformers import AutoTokenizer

def chunk_text(text, model_name="facebook/bart-large-cnn", max_tokens=1024, overlap=50):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.encode(text, add_special_tokens=False)
    
    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_text)
        start += max_tokens - overlap
        
    return chunks
