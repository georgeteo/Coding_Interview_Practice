# Rearrange string so that all characters are d distance away

### Algorithm

1. Traverse string and count frequencies of each character.
2. Store in a max heap (letter + frequency)
3. Pop from max heap and store in output array as p, p + d, ... for frequency number of times.
