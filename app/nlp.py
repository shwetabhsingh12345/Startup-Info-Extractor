from transformers import pipeline

qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

def extract_information(text):
    questions = {
        "description": "What does the startup do?",
        "industry": "What industry is the startup in?",
        "customers": "Who are the customers of the startup?",
        "funding": "Has the startup raised funds before?",
        "geography": "Where is the startup located?"
    }
    answers = {}
    for key, question in questions.items():
        result = qa_pipeline(question=question, context=text)
        answers[key] = result['answer']
    return answers

if __name__ == '__main__':
    text = "Input some sample text here."
    print(extract_information(text))
