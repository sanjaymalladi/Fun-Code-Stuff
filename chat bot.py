import openai
import requests

# Initialize the OpenAI API client with your API key
openai.api_key = "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"

def respond(prompt):
    if "search" in prompt.lower():
        query = prompt.split("search", 1)[1].strip()
        search_result = search(query)
        return search_result
    else:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        return response

def search(query):
    # Use the Google search API to find the top result for the query
    response = requests.get(f"https://www.google.com/search?q={query}")
    response.raise_for_status()
    result = response.text
    
    # Extract the top result from the search page HTML
    start_index = result.find("<a href=")
    end_index = result.find("</a>")
    top_result = result[start_index:end_index].strip()
    
    return top_result

# Start the chat loop
while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Bot: " + response)
