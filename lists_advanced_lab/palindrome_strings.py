words = input().split()
searched_palindrome = input()

found_palindromes = [word for word in words if word == word[::-1]]
count_palindromes = found_palindromes.count(searched_palindrome)

print(found_palindromes)
print(f'Found palindrome {count_palindromes} times')