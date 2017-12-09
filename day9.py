import re
with open("day9input.txt") as open_file:
    data = open_file.read()

# remove double negatives
data_clean = re.sub(r'!!', '', data)
# remove negated characters
data_clean1 = re.sub(r'![^\s]', '', data_clean)
#remove rubbish
data_clean2 = re.sub(r'<[^\s\>]*>', '', data_clean1)
# get braces
braces = re.findall(r'[\{\}]', data_clean2)
open_braces = []
score = 0
for brace in braces:
    if brace == "{":
        open_braces.append("{")
    else:
        if open_braces:
            score += len(open_braces)
            open_braces.pop()
print(score)

rubbish_length =0
all_rubbish = re.findall(r'<[^\s\>]*>', data_clean1)
for rubbish in all_rubbish:
    rubbish_length += len(rubbish)-2

print(rubbish_length)