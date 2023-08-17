def delete_nth(order,max_e):
    coj = set(order)
    coj = list(order)
    reverse = order[::-1]

    for i in range(len(coj)):
        count = reverse.count(coj[i])
        if count > max_e:
            for j in range(count - max_e):
                reverse.remove(coj[i])
    
    reverse = reverse[::-1]

    return reverse

print(delete_nth([20,37,20,21], 1))