import time

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)
    return z2 * 10**(2*m) + ((z1 - z2 - z0) * 10**m) + z0

def standard_multiplication(x, y):
    return x * y

start_time = time.time()
result_karatsuba = karatsuba(1234, 5678)
end_time_karatsuba = time.time()
print(f"Karatsuba result: {result_karatsuba}, Time: {end_time_karatsuba - start_time:.6f} seconds")

start_time = time.time()
result_standard = standard_multiplication(1234, 5678)
end_time_standard = time.time()
print(f"Standard multiplication result: {result_standard}, Time: {end_time_standard - start_time:.6f} seconds")

start_time = time.time()
result_karatsuba = karatsuba(123, 456789)
end_time_karatsuba = time.time()
print(f"Karatsuba result: {result_karatsuba}, Time: {end_time_karatsuba - start_time:.6f} seconds")

start_time = time.time()
result_standard = standard_multiplication(123, 456789)
end_time_standard = time.time()
print(f"Standard multiplication result: {result_standard}, Time: {end_time_standard - start_time:.6f} seconds")
