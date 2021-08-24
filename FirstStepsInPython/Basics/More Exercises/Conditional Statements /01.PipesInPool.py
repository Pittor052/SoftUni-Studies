v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

total_v = (h * p1) + (h * p2)
full = (total_v / v) * 100
overfull = total_v - v
pipe1_filled = ((h * p1) / total_v) * 100
pipe2_filled = ((h * p2) / total_v) * 100

if total_v <= v:
    print(f"The pool is {full:.2f}%  full. Pipe 1: {pipe1_filled:.2f}%. Pipe 2: {pipe2_filled:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {overfull} liters.")
