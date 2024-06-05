from django.shortcuts import render
from django.http import HttpResponse

def fibonacci(n):
    sequence = [0,1]
    while len(sequence)<n:
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def index(request):
    fib = fibonacci(20)
    prime = [i for i in range(1,101)if isprime(i)]
    message="First 10 numbers in fibonacci series: "+ ', '.join(map(str, fib))
    message1="Prime numbers between 1 and 100: "+ ', '.join(map(str, prime))
    return HttpResponse(message)
    



# Create your views here.
