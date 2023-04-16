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
    choice = input().rstrip().lower()
    if choice == 'i':
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open('input.txt', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    result = []
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return result
    prime = 1000000007
    x = 263
    p_hash = 0
    t_hash = 0
    x_p = pow(x, p_len, prime)
    for i in range(p_len):
        p_hash = (x * p_hash + ord(pattern[i])) % prime
        t_hash = (x * t_hash + ord(text[i])) % prime
    if p_hash == t_hash and pattern == text[:p_len]:
        result.append(0)
    for i in range(1, t_len - p_len + 1):
        t_hash = (t_hash - ord(text[i - 1]) * x_p % prime + prime) % prime
        t_hash = (t_hash * x + ord(text[i + p_len - 1])) % prime
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            result.append(i)
    return result



# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))