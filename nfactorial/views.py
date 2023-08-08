from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first, second):
    return HttpResponse(first + second)

def transform(request, text):
    return HttpResponse(text.upper())

def palindrome(request, word):
    return HttpResponse(word == word[::-1])

operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

def calculator(request, first, operation, second):
    return HttpResponse(operations[operation](first, second))