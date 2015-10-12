
def subset_generator(s):
    if len(s) <= 1:
        yield s
        yield []
    else:
        for item in subset_generator(s[1:]):
            yield [s[0]] + item
            yield item

if __name__=="__main__":
    test_list = [1,2,3]
    for subset in subset_generator(test_list):
        print subset
