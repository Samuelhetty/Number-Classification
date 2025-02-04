import requests
from django.http import JsonResponse
from django.views import View
from django.urls import path

NUMBERS_API_URL = "http://numbersapi.com/"

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number (only for non-negative numbers)."""
    if n < 0:
        return False  # Armstrong numbers are only for non-negative integers
    
    digits = [int(d) for d in str(abs(n))]  # Use abs(n) to remove the negative sign
    power = len(digits)
    return sum(d ** power for d in digits) == n


def get_number_fact(n):
    """Fetch a fun fact about the number from Numbers API."""
    try:
        response = requests.get(f"{NUMBERS_API_URL}{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fact found.")
    except requests.RequestException:
        return "Fact unavailable."
    return "Fact unavailable."

class ClassifyNumberView(View):
    """API View to classify numbers."""
    def get(self, request):
        number = request.GET.get("number")

        # Validate input
        if number is None or not number.lstrip("-").isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)

        number = int(number)  # Convert to integer safely after validation
        digit_sum = sum(int(d) for d in str(abs(number)))  # Use abs() for negatives
        properties = []

        # Identify number properties
        if is_armstrong(number):
            properties.append("armstrong")
        if is_prime(number):
            properties.append("prime")
        if is_perfect(number):
            properties.append("perfect")
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        # Construct response data
        data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": get_number_fact(number),
        }

        return JsonResponse(data)
