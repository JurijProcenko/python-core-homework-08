# Store people's favorite languages. 
fav_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name in sorted(fav_languages.keys()): 
    print(name + ": " + fav_languages[name])