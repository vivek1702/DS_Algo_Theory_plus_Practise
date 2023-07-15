def square_if_even_else_cube_if_odd(n):
    if n % 2 == 0:
        return n **2
    else:
        return n **3

print(square_if_even_else_cube_if_odd(3))