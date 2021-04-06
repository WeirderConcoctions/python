#Enter a word and check if the entered word is a palindrome or not
string = input("Enter word to be checked here: ").strip()
if string == string[::-1]:
   print("The entered word is a palindrome.\nYou won't be thanked for using Palindrome Checker\nHope you don't have Aibohphobia- a fear of palindromes")
else:
   print("The entered word is not a palindrome.\nYou won't be thanked for using Palindrome Checker")
