import re


import requests
def twitter(company,position):

    query ='site:twitter.com "Software developer" "Microsoft" in bio -inurl:status'

    url = f"https://www.google.com/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': 'YOUR_COOKIE_HERE'
    }
    response = requests.get(url, headers=headers)   

    # Define the regex pattern to find Twitter URLs
    pattern = r'https://twitter.com[^\s"\'<>]+'

    # Find all matches in the content
    matches = re.findall(pattern, response.text)
    filtered_matches = [match for match in matches if '&' not in match and ';' not in match and '\\' not in match]
    set(filtered_matches)

    # List to hold the JSON objects
    json_objects = []

    # Process each link
    for link in links:
        # Extract the last word from the link
        name = link.split('/')[-1]
        
        # Create a dictionary for the JSON object
        json_object = {
            "name": name,
            "position": "Software Engineer",
            "links": link
        }
        
        # Add to the list of JSON objects
        json_objects.append(json_object)

    # Convert list of JSON objects to a JSON string
    json_string = json.dumps(json_objects, indent=4)

    # Print or save the JSON string
    print(json_string)




