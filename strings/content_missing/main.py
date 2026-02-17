string = "It can be painful to learn from mistakes"

# Extract necessary words
learn = string[string.index('learn'):string.index('learn') + 5]
painful = string[string.index('painful'):string.index('painful') + 7]
mistakes = string[string.index('mistakes'):string.index('mistakes') + 8]


print("The variable learn equals:", learn)
print("The variable painful equals:", painful)
print("The variable mistakes equals:", mistakes)