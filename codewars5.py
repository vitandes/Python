def find_needle(haystack):
    
    if haystack[0] == "needle" :
        return 0
    
    position = find_needle(haystack[1:])
    
    
    position += 1
    
    
    return position


a = find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])
print(f"found the needle at position {a}")