import webbrowser

# Replacing using the .replace(' ','+')
# Replacing all Occurrences with the space with plus sign:
# Example: python programmer would be python+programming:
user_term = input('Enter the Search Term').replace(' ', '+')

webbrowser.open("https://www.google.com/search?q=" + user_term)
