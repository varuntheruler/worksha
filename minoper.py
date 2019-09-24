def min_number_of_operators(a,n):
    count = 0
    i =0
    j=n-1
    while(i<=j):
        if a[i] == a[j]:
            i = i+1
            j = j-1
        elif a[i]>a[j]:
            j =j-1
            a[j] = a[j]+a[j+1]
            count+=1
        else:
            i = i+1
            a[i]+=a[i-1]
            count+=1
    return count
a =list(map(int,input().split()))
n = len(a)
print(min_number_of_operators(a,n))

        
