'''You are tasked with designing a Python function that counts the number of words in a given sentence. 
The sentences may contain commas, full stops, and words enclosed in double quotes, and your function should be able to handle these scenarios.
Your function should take a sentence as input and return the count of words. Each word is separated by commas and full stops, and words enclosed in double quotes should be treated as single entities.
'''

'''import re

def count_words(sentence):
    # Use regular expression to split the sentence into words
    words = re.findall(r'\b\w+\b|"[^"]*"', sentence)

    # Count the number of words
    word_count = len(words)

    return word_count

# Example usage:
sentence = 'This is a sample sentence, with some "quoted words." It has commas and full stops.'
result = count_words(sentence)
print(f'The number of words in the sentence is: {result}')'''

import openai
openai.api_key='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'

user_prompt='Give me information about slowly changing dimension in dwh'
response = openai.Completion.create(
    engine="davinci",
    prompt=f"Generate recommendations for companies: {user_prompt}",
    max_tokens=150
)
print(response.choices[0].text.strip())


