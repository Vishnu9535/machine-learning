# import spacy
# import fuzzywuzzy
# from fuzzywuzzy import fuzz

# # Load the spaCy language model
# nlp = spacy.load('en_core_web_sm')

# # List of country names
# countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]



# # Input string


# s = "Repubic of congo"

# # Initialize a list to store extracted country names
# matched_countries = []

# # Process the input string using spaCy
# doc = nlp(s.lower())

# # Tokenize the input string
# tokens = [token.text for token in doc]

# # Iterate through the tokens
# for i in range(len(tokens)):
#     for j in range(i, len(tokens)):
#         candidate = ' '.join(tokens[i:j + 1])
#         # Use fuzzy matching to check similarity with country names
#         for country in countries:
#             similarity = fuzz.partial_ratio(candidate, country)
#             if similarity >= 80:  # Adjust the similarity threshold as needed
#                 matched_countries.append(country)

# # Remove duplicate country names
# matched_countries = list(set(matched_countries))

# # Print the extracted country names
# print("Matched countries:", matched_countries)

# import spacy
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load the spaCy language model
# nlp = spacy.load('en_core_web_sm')

# # List of country names
# countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]

# # Input string
# s = "Repubicofusa"

# # Tokenize the input string using spaCy
# doc = nlp(s.lower())
# input_tokens = [token.text for token in doc]

# # Tokenize country names
# country_tokens = [nlp(country.lower()) for country in countries]

# # Combine tokens into strings for TF-IDF
# country_strings = [' '.join([token.text for token in country]) for country in country_tokens]

# # Initialize TF-IDF vectorizer
# vectorizer = TfidfVectorizer()

# # Fit and transform the TF-IDF vectorizer on country names
# tfidf_matrix = vectorizer.fit_transform(country_strings)

# # Transform the input string using the same vectorizer
# input_tfidf = vectorizer.transform([' '.join(input_tokens)])

# # Calculate cosine similarity between the input and country names
# cosine_similarities = cosine_similarity(input_tfidf, tfidf_matrix)

# # Find the index of the most similar country name
# most_similar_index = cosine_similarities.argmax()

# # Extract the matched country name
# matched_country = countries[most_similar_index]

# # Print the matched country name
# print("Matched country:", matched_country)

# from fuzzywuzzy import fuzz

# # List of country names
# countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]

# # Input string
# s = "Repubicofusa"

# # Initialize a list to store matched country names
# matched_countries = []

# # Iterate through the country names and calculate similarity
# for country in countries:
#     similarity = fuzz.partial_ratio(s.lower(), country.lower())
#     if similarity >= 80:  # Adjust the similarity threshold as needed
#         matched_countries.append(country)

# # Print the matched country names
# print("Matched countries:", matched_countries)
# import spacy
# # import fuzzywuzzy
# from fuzzywuzzy import fuzz

# # Load the spaCy language model
# nlp = spacy.load('en_core_web_sm')

# # List of country names
# countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]

# # Input string
# s = "brazil czech republic"

# # Initialize a list to store extracted country names
# matched_countries = []

# # Process the input string using spaCy
# doc = nlp(s.lower())

# # Tokenize the input string
# tokens = [token.text for token in doc]

# # Iterate through the tokens
# for i in range(len(tokens)):
#     for j in range(i, len(tokens)):
#         candidate = ' '.join(tokens[i:j + 1])
#         # Use fuzzy matching to check similarity with country names
#         for country in countries:
#             similarity = fuzz.partial_ratio(candidate, country)
#             if similarity >= 80:  # Adjust the similarity threshold as needed
#                 matched_countries.append(country)

# # Remove duplicate country names
# matched_countries = list(set(matched_countries))

# # Print the extracted country names
# print("Matched countries:", matched_countries)
# import spacy
# from fuzzywuzzy import fuzz

# # Load the spaCy language model
# nlp = spacy.load('en_core_web_sm')

# # List of country names
# countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]

# # Input string
# s = "brazil czech republic"

# # Initialize a set to store extracted country names
# matched_countries = set()

# # Process the input string using spaCy
# doc = nlp(s.lower())

# # Tokenize and join the tokens to form candidate phrases
# tokens = [token.text for token in doc]
# candidates = [' '.join(tokens[i:j+1]) for i in range(len(tokens)) for j in range(i, len(tokens))]

# # Use fuzzy matching to check similarity with country names
# for candidate in candidates:
#     for country in countries:
#         similarity = fuzz.partial_ratio(candidate, country)
#         if similarity >= 80:  # Adjust the similarity threshold as needed
#             matched_countries.add(country)

# # Convert the set of matched countries to a list
# matched_countries = list(matched_countries)

# # Print the extracted country names
# print("Matched countries:", matched_countries)
import spacy
from fuzzywuzzy import fuzz

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# List of country names
countries = ["brazil", "czech republic", "republic of usa", "South Korea", "North Korea"]

# Input string
s = "brazil czech republic usa south korea"

# Initialize a set to store extracted country names
matched_countries = set()

# Process the input string using spaCy
doc = nlp(s.lower())

# Tokenize and join the tokens to form candidate phrases
tokens = [token.text for token in doc]
candidates = [' '.join(tokens[i:j + 1]) for i in range(len(tokens)) for j in range(i, len(tokens))]

# Sort the candidates by length (shortest to longest)
candidates.sort(key=len)

# Use fuzzy matching to check similarity with country names
for candidate in candidates:
    for country in countries:
        similarity = fuzz.partial_ratio(candidate, country)
        if similarity >= 80:  # Adjust the similarity threshold as needed
            matched_countries.add(country)
            break  # Break to avoid matching longer country names

# Convert the set of matched countries to a list
matched_countries = list(matched_countries)

# Print the extracted country names
print("Matched countries:", matched_countries)

