# Miller Rabin Algorithm

Miller-Rabin Primality Test Algorithm

Implemented by: [@mertkosan](https://github.com/mertkosan)

### Getting Started

    NOTE: This application is implemented in Python 2.7x

This program takes two arguments:
1. n : the number whose primality will be tested.
2. t : the number of trials that first argument will be tested.

    
    python main.py -n 221 -t 10
    
    this command is looking for whether 221 is prime or not with 10 number of trials
    
If t is not specified, it is equal to 1.

If n is not specified, the number, in range 5 and 2^1024, will be randomly found and tested, until it returns 'inconclusive'. 
After the finding 'inconclusive' answer, that number will be tested t (number of trials) times.

When program terminates, it prints the number and the result.
Number indicates the test number.
Result indicates whether the number is prime or not. If 'composite' is printed, the number is composite. If 'inconclusive'
is printed, the number is prime quite likely.