"""Return True if the number is a prime number, otherwise False."""

def is_prime(number: int) -> bool:
    if number <= 1:
        return False  
    for i in range(2, int(number**0.5) + 1): 
        if number % i == 0: 
            return False 
    return True 
print(is_prime(13)) 