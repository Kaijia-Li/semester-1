# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


seq = [0]

for i in range(1, L):
    next_val = seq[-1] - i
    if next_val > 0 and next_val not in seq:
        seq.append(next_val)
    else:
        seq.append(seq[-1] + i)

print(seq)
# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in seq]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence