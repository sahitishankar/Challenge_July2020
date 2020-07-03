#1+2+3...n = n(n+1)/2

def arrcoins(n):
    left = 0
    right = n
    while left <= right:
        k = (left + right) // 2
        curr = k*(k+1) // 2
        if n == curr:
            return k
        if n < curr:
            right = k - 1
        else: 
            left = k + 1
    return right
    
    
    
print(arrcoins(5))
print(arrcoins(8))
print(arrcoins(6))
print(arrcoins(10))
print(arrcoins(1))

