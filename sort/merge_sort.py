def sort(list_to_order):
    if len(list_to_order)>1:
        mid = len(list_to_order)//2
        left_thalf = list_to_order[:mid]
        righ_thalf = list_to_order[mid:]

        sort(left_thalf)
        sort(righ_thalf)
        _merge(left_thalf,righ_thalf,list_to_order)

def _merge(left_half,right_half,list_to_order):
    i=j=k=0       
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            list_to_order[k] = left_half[i]
            i=i+1
        else:
            list_to_order[k] = right_half[j]
            j=j+1
        k=k+1

    while i < len(left_half):
        list_to_order[k] = left_half[i]
        i=i+1
        k=k+1

    while j < len(right_half):
        list_to_order[k] = right_half[j]
        j=j+1
        k=k+1
            

nlist = [14,46,43,27,57,41,45,21,70]
sort(nlist)
print(nlist)