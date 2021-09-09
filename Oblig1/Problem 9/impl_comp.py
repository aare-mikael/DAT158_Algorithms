# Problem 9c
from lcs_dp import lcs_dp
from lcs_rec import lcs_rec
import time
import random
import json
import string

def writeToFile(arr, name):
    with open('{}.json'.format(name), 'w', encoding='utf-8') as f:
        json.dump(arr, f, indent=4)

if __name__ == '__main__':

    X = ""
    Y = ""
    i = 0
    rec_times = []
    dp_times = []

    # Length of X and Y is equal to i.
    while i < 32:
        chars = string.ascii_lowercase  # "ab"
        X += random.choice(chars)
        Y += random.choice(chars)
        t = time.process_time()
        print("Recursive LCS: ", lcs_rec(X, Y, len(X), len(Y)))
        time_rec = time.process_time() - t
        rec_times.append(time_rec)
        t = time.process_time()
        print("DP LCS: ", lcs_dp(X, Y))
        time_dp = time.process_time() - t
        dp_times.append(time_dp)
        print("Time recursive: {} \nTime DP: {}".format(time_rec, time_dp))
        print("{} Finished Round {} {}".format(5*"-", i+1, 5*"-"), "\n")
        i += 1

    writeToFile(rec_times, "Recursive_Times")
    writeToFile(dp_times, "DP_Times")

    """
    For strings consisting of two unique characters, the recursive algorithm seems to slow when the strings lengths are around 28 to 32. 
    For strings consisting of more than two unique characters, the recursive algorithm seems to slow when string length is around 13-15.
    The worst case time complexity of the recursive approach is O(2^n+m).
    This corresponds with my findings, as iterative rounds usually takes 4 times longer than the previous. 
    See the pictures in the repo for examples, or run this file with your own settings.
    """

    """
Recursive LCS:  0
DP LCS:  0
Time recursive: 0.0 
Time DP: 0.0
----- Finished Round 1 ----- 

Recursive LCS:  1
DP LCS:  1
Time recursive: 0.0 
Time DP: 0.0
----- Finished Round 2 ----- 

Recursive LCS:  1
DP LCS:  1
Time recursive: 0.0
Time DP: 0.0
----- Finished Round 3 -----

Recursive LCS:  1
DP LCS:  1
Time recursive: 0.0
Time DP: 0.0
----- Finished Round 4 -----

Recursive LCS:  1
DP LCS:  1
Time recursive: 0.0
Time DP: 0.0
----- Finished Round 5 -----

Recursive LCS:  1
DP LCS:  1
Time recursive: 0.0
Time DP: 0.0
----- Finished Round 6 -----

Recursive LCS:  1
DP LCS:  1
Time recursive: 0.015625
Time DP: 0.0
----- Finished Round 7 -----

Recursive LCS:  2
DP LCS:  2
Time recursive: 0.0
Time DP: 0.0
----- Finished Round 8 -----

Recursive LCS:  2
DP LCS:  2
Time recursive: 0.0
Time DP: 0.0
----- Finished Round 9 -----

Recursive LCS:  2
DP LCS:  2
Time recursive: 0.015625
Time DP: 0.0
----- Finished Round 10 -----

Recursive LCS:  2
DP LCS:  2
Time recursive: 0.09375
Time DP: 0.0
----- Finished Round 11 -----

Recursive LCS:  3
DP LCS:  3
Time recursive: 0.25
Time DP: 0.0
----- Finished Round 12 -----

Recursive LCS:  3
DP LCS:  3
Time recursive: 0.765625
Time DP: 0.0
----- Finished Round 13 -----

Recursive LCS:  3
DP LCS:  3
Time recursive: 2.921875
Time DP: 0.0
----- Finished Round 14 -----

Recursive LCS:  4
DP LCS:  4
Time recursive: 9.234375
Time DP: 0.0
----- Finished Round 15 -----

Recursive LCS:  4
DP LCS:  4
Time recursive: 36.125
Time DP: 0.0
----- Finished Round 16 -----
    """