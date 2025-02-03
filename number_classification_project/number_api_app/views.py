import requests
from django.http import JsonResponse
from django.views import View
from django.urls import path

NUMBERS_API_URL = "http://numbersapi.com/"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_number_fact(n):
    try:
        response = requests.get(f"{NUMBERS_API_URL}{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fact found.")
    except requests.RequestException:
        return "Fact unavailable."
    return "Fact unavailable."

class ClassifyNumberView(View):
    def get(self, request):
        number = request.GET.get("number")
        
        # Check if the 'number' parameter is missing or not a valid number
        if not number or not number.isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)
        
        number = int(number)
        properties = []
        
        # Check if the number is Armstrong
        if is_armstrong(number):
            properties.append("armstrong")
        
        # Check if the number is even or odd
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        
        # Construct the result dictionary
        result = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(number)),
            "fun_fact": get_number_fact(number)
        }
        
        return JsonResponse(result)
