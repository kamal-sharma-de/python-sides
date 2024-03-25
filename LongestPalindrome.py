def longest_palindromic_substring(text):
  """
  Finds the longest palindromic substring within a given text string.
  Time complexity: O(n^2), where n is the length of the text string.
  """

  n = len(text)
  longest_palindrome = ""

  # Iterate through all possible starting and ending indices of substrings
  for i in range(n):
    for j in range(i, n):
      substring = text[i:j+1]
      # Check if the substring is a palindrome
      if substring == substring[::-1] and len(substring) > len(longest_palindrome):
        longest_palindrome = substring

  return longest_palindrome

text = "racecarannakayak"
longest_palin = longest_palindromic_substring(text)
print("Longest palindromic substring:", longest_palin)
print("Time complexity: O(n^2)")
