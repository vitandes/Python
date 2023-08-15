def to_camel_case(text):
    
    if len(text) == 0:
        return ""
    
    camelCase = text.title()
    array = list(camelCase)
    
    array[0] = list(text)[0]
    
   
    agroup = "".join(array) 
    agroup = "".join(c for c in agroup if c != "-" and c !="_") 
    
    return agroup

print(to_camel_case("the_stealth_warrio"))
