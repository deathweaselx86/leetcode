from collections import defaultdict

class Solution:    
    def getHint(self, secret: str, guess: str) -> str:
        secret_list = list(secret)
        guess_list = list(guess)
        bull_count = 0
        cow_count = 0
        
        
        # first get bulls
        # to get a count, we can directly compare digits in the string
        for i in range(len(guess_list)):
            if secret_list[i] == guess_list[i]:
                # to avoid counting bulls as cows
                #    - remove matched digits from both strings
                guess_list[i] = None
                secret_list[i] = None
                bull_count+=1
        
        # next, find instances of the remaining digits in the guess
        # create histogram of digits from the secret
        secret_histogram = defaultdict(int)
        for ch in secret_list:
            if ch:
                secret_histogram[ch]+=1
        print(guess_list)
        print(secret_histogram)
        for ch in guess_list:
            if ch and secret_histogram[ch] > 0:
                cow_count+=1
                secret_histogram[ch] = secret_histogram[ch] - 1
        
        return f'{bull_count}A{cow_count}B'