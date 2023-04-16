# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    choice = input()

    if 'I' in choice:
        pattern = input().rstrip()
        text = input().rstrip()

    elif 'F' in choice:
        with open("tests/06", "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    else:
        print('wrong input')
        return
    
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    pattern_len = len(pattern)
    text_len = len(text)

    pattern_hash = 0
    for i in range(pattern_len):
        pattern_hash += ord(pattern[i]) * pow(101, i)

    window_hash = 0
    for i in range(pattern_len):
        window_hash += ord(text[i]) * pow(101, i)
    
    result = []

    if pattern_hash == window_hash and pattern == text[:pattern_len]:
        result.append(0)

    for i in range(1, text_len - pattern_len + 1):
        window_hash -= ord(text[i - 1])
        window_hash //= 101
        window_hash += ord(text[i + pattern_len - 1]) * pow(101, pattern_len - 1)

        if pattern_hash == window_hash and pattern == text[i:i+pattern_len]:
            result.append(i)

    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))