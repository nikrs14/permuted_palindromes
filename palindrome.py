from itertools import permutations as perms

def palindrome(a):

    score = 0

    initial_array = list()
    another_array = list()
    final_array = list()

    for char in a:
        initial_array.append(char)
    
    if len(initial_array) <= 10:
    
        perm_list = perms(initial_array)

        for permutation in list(perm_list):
            another_array.append(permutation)
        
        for permutation in another_array:
            count = 0
            if permutation == permutation[:: -1]:
                for element in final_array:
                    if permutation == element:
                        count += 1
                if count == 0:
                    score += 1
                    final_array.append(permutation)
        
        if score == 0:
            print("I didn't find any palindrome.")
        else:
            for element in final_array:
                print("I found a palindrome! It's", end=' ')
                for char in element:
                    print(char, end='')
                print("")
            print(f"This word has {score} permuted palindromes.")

    else:
        print("Too many characters.")


print("Welcome to the Palindrome Characters Checker.")

while True:
    while True:
        try:
            string = str(input("What is the word? ")).lower()
            break
        except ValueError:
            print("Try again.")

    palindrome(string)

    while True:
        try:
            answer = str(input("Do you want to do it again? ")).strip().lower()
            assert answer == "yes" or answer == "no"
            break
        except AssertionError:
            print("Try again.")
        
    if answer == 'no':
        break
