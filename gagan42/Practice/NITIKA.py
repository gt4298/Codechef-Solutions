T = int(input().strip())
 
for i in range(T):
    name = input().strip().lower()
    arr = name.split(" ")
    ans = ""
    for j in range(len(arr) - 1):
        ans += (arr[j][0].upper() + ". ")
    ans+= arr[len(arr) -1][0].upper() + arr[len(arr) -1][1:]
    print(ans)
