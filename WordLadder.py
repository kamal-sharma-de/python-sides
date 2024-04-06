from collections import deque

def word_ladder(beginWord, endWord, wordList):
  """
  Args:
      beginWord: The starting word.
      endWord: The target word.
      wordList: A set of valid words.

  Returns:
      A list of words representing the shortest word ladder, or an empty list if no ladder exists.
  """
  queue = deque([(beginWord, 1)])  # (word, level)
  visited = set()

  while queue:
    current_word, level = queue.popleft()
    visited.add(current_word)

    if current_word == endWord:
      # Build the ladder by backtracking from endWord
      ladder = [current_word]
      while level > 1:
        for next_word in visited:
          if len(next_word) == len(current_word) and sum(a != b for a, b in zip(next_word, current_word)) == 1:
            ladder.append(next_word)
            current_word = next_word
            break
      return ladder[::-1]  # Reverse the ladder for correct order

    for i in range(len(current_word)):
      # Generate all possible neighbors by changing one letter
      for char in 'abcdefghijklmnopqrstuvwxyz':
        next_word = current_word[:i] + char + current_word[i+1:]
        if next_word in wordList and next_word not in visited:
          queue.append((next_word, level + 1))

  return []  # No word ladder found

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = {"hot", "dot", "dog", "lot", "log", "cog"}

word_ladder_result = word_ladder(beginWord, endWord, wordList)
print(word_ladder_result)  # Output: ["hit", "hot", "dot", "dog", "cog"]
