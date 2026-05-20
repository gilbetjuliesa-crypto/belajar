n = int(input())
words = [input() for _ in range(n)]

x = set()
result = "Fair Game"

for i, word in enumerate(words):
    player = (i % 2) + 1  


    if word in x:
        result = f"Player {player} lost"
        break

    if i > 0:
        prev_word = words[i - 1]
        if word[0] != prev_word[-1]:
            result = f"Player {player} lost"
            break

    x.add(word)

print(result)