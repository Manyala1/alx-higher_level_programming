#!/usr/bin/python3
def search_replace(my_list, search, replace):
  """
  Replaces all occurrences of `search` element with `replace` element in a new list.

  Args:
      my_list: A list of any type of elements.
      search: The element to be replaced.
      replace: The new element to replace with.

  Returns:
      A new list with all occurrences of `search` replaced by `replace`.
  """
  new_list = []
  for element in my_list:
    if element == search:
      new_list.append(replace)
    else:
      new_list.append(element)
  return new_list
