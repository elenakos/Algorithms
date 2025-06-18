'''
Write a script that captures HTML from a page and checks if a given word is present.
'''

import requests

url = 'https://www.python.org/'
text_to_find = "python"

try:
    response = requests.get(url)
    html_text = response.text

    if text_to_find in html_text:
        print("Found the word!")
        count = 0
        for word in html_text.split():
            if text_to_find.lower() in word.lower():
                count += 1
        print(f'The word "{text_to_find}" was found in {count} words.')
    else:
        print("Sorry, the word is not present!")
except Exception as e:
    print(e)




