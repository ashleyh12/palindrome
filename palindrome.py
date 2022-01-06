def is_palindrome(string):
  if string[::-1] == string[::1]: #compares the string forwards and backwards (for the strings w/o spaces)
    return True  
  elif ' ' in string: #this elif statement and the following lines determines whether a string (with spaces) is a palindrome 
      space_string = string.replace(" ", "")
      if space_string[::-1] == space_string[::1]:
        return True
      else:
        return False
  else:
    return False

print(is_palindrome("a man a plan a canal panama"))

