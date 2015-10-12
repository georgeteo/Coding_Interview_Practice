def generate_permutations(string):
    if len(string) == 1:
        return [string]
    first_letter = string[0]
    remaining_letters = generate_permutations(string[1:])
    return_value = []
    for permutation in remaining_letters:
        for i in range(len(permutation)+1):
            return_value.append(permutation[:i] + first_letter + permutation[i:])
    return return_value
