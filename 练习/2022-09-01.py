a=[1234,413623,723,54,16513,46,1353416,15231,512,22222222222222222222222222,33,34613,451,541,24613,4613,45123,222,223]
a.sort(key=int,reverse=False)
t_m=a[1]-a[0]
for i in a:
    if i==a[-1]:
        break
    else:
        mi=a[a.index(i)+1]-i
        if t_m>mi:
            t_m=mi
print(t_m)