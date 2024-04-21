def explore_dictionaries(data):
  """
  This function explores the functionalities and use cases of dictionaries.

  Args:
      data: A dictionary containing key-value pairs.

  Returns:
      A dictionary with information about the explored functionalities.
  """

  results = {}

  # Accessing Elements (by key)
  try:
    name = data["name"]
    results["access_by_key"] = f"Successfully retrieved value: {name}"
  except KeyError:
    results["access_by_key"] = "Key 'name' not found in the dictionary."

  # Modifying Elements (updating existing key)
  data["age"] = data.get("age", 0) + 1  # Increment age if it exists, set to 1 if not
  results["modify_element"] = f"Dictionary after modification: {data}"

  # Adding New Elements
  data["city"] = "New York"
  results["add_element"] = f"Added new key-value pair: 'city':'New York'"

  # Removing Elements (by key)
  if "occupation" in data:
    del data["occupation"]
    results["remove_element"] = "Removed key 'occupation'"
  else:
    results["remove_element"] = "Key 'occupation' not found in the dictionary."

  # Checking Key Existence
  has_email = "email" in data
  results["check_key_existence"] = f"Key 'email' exists: {has_email}"

  # Looping through Key-Value Pairs
  for key, value in data.items():
    print(f"Key: {key}, Value: {value}")
  results["looping"] = "Successfully iterated through key-value pairs (printed separately)"

  # Merging Dictionaries (combining key-value pairs)
  additional_data = {"skills": ["Python", "Java"]}
  merged_data = {**data, **additional_data}
  results["merge_dictionaries"] = f"Merged dictionary: {merged_data}"

  return results

# Example Usage
data = {"name": "Alice", "age": 30, "occupation": "Software Engineer"}
exploration_results = explore_dictionaries(data.copy())  # Avoid modifying original data

print("Exploration Results:")
for key, value in exploration_results.items():
  print(f"{key.upper()}: {value}")
