length = int(input())
width = int(input())
height = int(input())
volume_lose = float(input())
volume = length * width * height
litres = volume / 1000
volume_lose = volume_lose * 0.01
litres_needed = litres *(1 - volume_lose)
print(litres_needed)