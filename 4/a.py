tiga_point_w = int(input())
two_point_w = int(input())
free_point_w = int(input())

total_wisnu = tiga_point_w * 3 + two_point_w * 2 + free_point_w

tiga_point_s = int(input())
two_point_s = int(input())
free_point_s = int(input())

total_s = tiga_point_s * 3 + two_point_s * 2 + free_point_s

if total_wisnu > total_s:
    print("W")
elif total_s > total_wisnu:
    print("S")
else:
    print("X")