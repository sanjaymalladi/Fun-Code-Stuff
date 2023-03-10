import openai
import PyPDF2
import requests


# replace YOUR_API_KEY with your actual API key for the ChatGPT service
openai.api_key = "YOUR_API_KEY"

def read_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        text = ""
        for i in range(pdf.getNumPages()):
            page = pdf.getPage(i)
            text += page.extractText()
        return text

def summarize_pdf_gpt3(pdf_path):
    text = read_pdf(pdf_path)
    # Use GPT-3 to summarize text
    prompt = (f"Please summarize this text: {text}")
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        json={
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens":150,
            "top_p":1,
            "frequency_penalty":1,
            "presence_penalty":1
        },
        headers={"Authorization": f"Bearer {secrets['api_key']}"}
    ).json()
    return response["choices"][0]["text"].strip()

pdf_path = "path/to/pdf/file.pdf"
summary = summarize_pdf_gpt3(pdf_path)
print(summary)
