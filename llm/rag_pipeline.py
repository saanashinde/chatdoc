from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load a pretrained LLM from Hugging Face
model_name = "distilgpt2"  # Or try "mistralai/Mistral-7B-Instruct-v0.2" if resources allow
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

qa_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_answer(context, query):
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    result = qa_pipeline(prompt, max_length=200, do_sample=True, top_k=50)[0]["generated_text"]
    return result.split("Answer:")[-1].strip()
