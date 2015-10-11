def count_solution(real_solution, guess):
    guess_list = list(guess)
    number_correct = 0
    number_pseudocorrect = 0
    accumulator = {}
    i = 0
    for letter in real_solution:
        if guess_list[i] == letter:
            number_correct += 1
            del guess_list[i]
            i -= 1
        else:
            try:
                accumulator[letter] += 1
            except:
                accumulator[letter] = 1
        i += 1
    for remaining_letter in guess_list:
        try:
            if accumulator[letter] == 0:
                del accumulator[remaining_letter]
                continue
            accumulator[letter] -= 1
            number_pseudocorrect += 1
        except:
            pass
    return number_correct, number_pseudocorrect

if __name__=="__main__":
    number_correct, number_pseudocorrect = count_solution("YYYG", "YGBR")
    print "Expect 1 - got {}".format(number_correct)
    print "Expect 1 - got {}".format(number_pseudocorrect)
