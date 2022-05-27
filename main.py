# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    # [assignment] Add your code here
    user_input_1 = input("enter a word")
    user_input_2 = input("enter another word")
    n1 = len(user_input_1)
    n2 = len(user_input_2)
  
    if n1 == n2:
        return True
  
    user_input_1 = sorted(user_input_1)
    user_input_2 = sorted(user_input_2)
  
    for i in range(0, n2):
        if user_input_1[i] != user_input_2[i]:
            return False

