def find_Anagram():
    first_word = input("Enter first word: ")
    second_word = input("Enter second word: ")

    if len(first_word) != len(second_word): return "The words are not of equal length."

    for char in first_word:
        if char not in second_word:
            return False
    return True
i = "yes"
while i == "yes":
    print(find_Anagram())
    i = input("Do you want to continue (yes/no) :")

        
