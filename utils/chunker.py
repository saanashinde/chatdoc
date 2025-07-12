import spacy
nlp = spacy.load("en_core_web_sm")

def chunk_text(text, chunk_size=300, overlap=50):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        length = len(sentence.split())
        if current_length + length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            current_length = sum(len(s.split()) for s in current_chunk)

        current_chunk.append(sentence)
        current_length += length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
