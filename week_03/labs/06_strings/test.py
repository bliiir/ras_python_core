word = "barcelona Python 2018"

cap = word.capitalize()
fold = word.casefold()
center = word.center(80, "*")
count = word.count("arce", 0, 6)
encode = word.encode(encoding="utf-8", errors="strict")
ends = word.endswith("18")

print(ends)
