import difflib

varA = 'plaimountain'
varB = 'piaimauntain'
varC = 'skymountain'
varS = ['piaimauntain', 'sky', 'skymountain', 'dog', '231']

# it parse varB by letters
best = difflib.get_close_matches(varA, varB)
print(best)

best = difflib.get_close_matches(varA, [varB])
print(best)

best = difflib.get_close_matches(varA, [varB, varC])
print(best)

best = difflib.get_close_matches(varA, [varB, varS])
print(best)
