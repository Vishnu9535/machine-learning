import spacy
import fuzzywuzzy
from fuzzywuzzy import fuzz

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# List of country names
countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]

# Input string


s = "Repubic"

# Initialize a list to store extracted country names
matched_countries = []

# Process the input string using spaCy
doc = nlp(s.lower())

# Tokenize the input string
tokens = [token.text for token in doc]

# Iterate through the tokens
for i in range(len(tokens)):
    for j in range(i, len(tokens)):
        candidate = ' '.join(tokens[i:j + 1])
        # Use fuzzy matching to check similarity with country names
        for country in countries:
            similarity = fuzz.partial_ratio(candidate, country)
            if similarity >= 80:  # Adjust the similarity threshold as needed
                matched_countries.append(country)

# Remove duplicate country names
matched_countries = list(set(matched_countries))

# Print the extracted country names
print("Matched countries:", matched_countries)
