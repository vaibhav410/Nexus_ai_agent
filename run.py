from app import store_mood,suggest

m = input("Mood: ")
n = input("Reason: ")

store_mood(m, n)
print("Suggestion:", suggest(m))
