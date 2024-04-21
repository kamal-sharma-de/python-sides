def compare_data_structures(data):
  """
  This function compares the behavior of lists, tuples, and sets with the provided data.

  Args:
      data: Any Python object (list, tuple, set, or other data type)

  Returns:
      A dictionary containing information about the data structure used and its properties.
  """

  # Check data type and create copies for modification (avoid modifying original data)
  if isinstance(data, list):
    data_copy = data.copy()
    data_type = "List"
  elif isinstance(data, tuple):
    data_copy = data  # Tuples are immutable, cannot create a copy
    data_type = "Tuple"
  elif isinstance(data, set):
    data_copy = data.copy()
    data_type = "Set"
  else:
    return {"data_type": "Unsupported data type"}

  # Operations and Explanations
  results = {"data_type": data_type}

  # Mutability (can elements be changed?)
  try:
    data_copy[0] = "Modified"  # Attempt to modify first element
    results["mutability"] = "Mutable"
  except TypeError:
    results["mutability"] = "Immutable"

  # Ordering (is the order of elements preserved?)
  results["ordering"] = sorted(data_copy) == data_copy  # Check if order is preserved after sorting

  # Duplicates (can elements appear multiple times?)
  results["duplicates"] = len(set(data_copy)) != len(data_copy)  # Check if length changes after converting to set (removing duplicates)

  # Membership Testing (how fast can you check if an element exists?)
  element_to_find = "Apple"
  results["membership_test"] = element_to_find in data_copy  # Time complexity demonstration (not measured here)

  # Additional Notes (for sets)
  if data_type == "Set":
    results["notes"] = "Sets are unordered collections with unique elements. They are useful for checking element membership and performing set operations (union, intersection, difference)."

  return results

# Example Usage
data_list = ["Apple", "Banana", "Orange", "Apple"]
data_tuple = ("Apple", "Banana", "Orange")
data_set = {"Apple", "Banana", "Orange"}

list_results = compare_data_structures(data_list)
tuple_results = compare_data_structures(data_tuple)
set_results = compare_data_structures(data_set)

print("List Results:", list_results)
print("Tuple Results:", tuple_results)
print("Set Results:", set_results)
