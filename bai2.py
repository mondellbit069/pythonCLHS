a = list(map(int, input().split()))
avg = sum(a) / 12
print("Trung binh moi thang tieu la: ", avg)
if avg > 10**6: print("Tieu thu dien qua cao")
else: print("Tieu thu dien binh thuong")