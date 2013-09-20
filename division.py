#!/usr/bin/env python
#============================================================================================================

import os, sys
from itertools import product, count

def main(fixed_digit=7):
    x1_x3_range = range(fixed_digit+1, 10)
    x2_range = range(1,9)
    
    results = []

    for factor in count(100):
        if factor*fixed_digit >= 1000:
            break
        else:
            for x1,x2,x3 in product(x1_x3_range, x2_range, x1_x3_range):
                quotient = int(str(x3)+str(fixed_digit)+str(x2)+'0'+str(x1))
                base = quotient * factor
                base_str = str(base)
                if factor*x1 >= 1000 and factor*x2 < 1000 and factor*x3 >= 1000:
                    diff_1 = int(base_str[0:4]) - x3*factor
                    if diff_1 >= 10 and diff_1 < 100:
                        diff_2 = diff_1*10 + int(base_str[4]) - 7*factor
                        if diff_2 >= 100 and diff_2 < 1000:
                            diff_3 = diff_2*10 + int(base_str[5]) - x2*factor
                            if diff_3 >= 10 and diff_3 < 100 and diff_3*10 + int(base_str[6]) < factor:
                                results.append({'factor': factor,'quotient': quotient, 'base': base})
    return results

#============================================================================================================

if __name__ == '__main__':
    results = main(fixed_digit=int(sys.argv[1]))
    for result in results:
        print(result)

#============================================================================================================
# unique result:
# {'quotient': 97809, 'base': 12128316, 'factor': 124}
#============================================================================================================
