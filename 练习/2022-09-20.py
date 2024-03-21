def late_clock(digits):
    def loc_num(arr,n):
        req_num=req_idx=-1
        for k in range(len(arr)):
            if arr[k]<=n:
                if arr[k]>=req_num:
                    req_num=arr[k]
                    req_idx=k
        arr[req_idx]=-1
        return req_num

    from copy import deepcopy
    digits_copy=deepcopy(digits)

    t=[0]*4
    nl=[2,3,5,9]
    for i in range(len(nl)):
        if i==1:
            t[i]=loc_num(digits,nl[i] if t[i-1]==nl[i-1] else loc_num(digits,nl[i]**2))
        else:t[i]=loc_num(digits,nl[i])

    if min(t)<0:
        nl=[1,9,5,9]
        t=[loc_num(digits_copy,nl[i]) for i in range(len(nl))]

    return "%s%s:%s%s"%(t[0],t[1],t[2],t[3])

print(late_clock(digits=[1,2,3,8]))