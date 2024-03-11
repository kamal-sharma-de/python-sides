# Define a list of prompts and their corresponding word types
prompts = [
    ("a noun", "person"),
    ("an adjective", "descriptive"),
    ("a verb", "action"),
    ("an adverb", "descriptive"),
    ("a noun", "place"),
    ("a food", "funny"),
    ("a number", "any")
]

# Create an empty story template
story = "Once upon a time, there was a(n) {} named {}. They loved to {} {} in their {}. One day, they ate too much {} and had to eat {} times their size!"

# Loop through prompts and get user input
words = []
for prompt in prompts:
  word_type, descriptor = prompt
  word = input(f"Enter a {descriptor} {word_type}: ")
  words.append(word)

# Insert user words into the story template
formatted_story = story.format(*words)

# Print the completed story
print(formatted_story)
