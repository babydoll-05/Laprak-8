def anagram(kata1, kata2):
       
    kata1 = kata1.lower().replace(" ", "")
    kata2 = kata2.lower().replace(" ", "")

  
    if len(kata1) != len(kata2):
        return False

    
    return sorted(kata1) == sorted(kata2)


print(anagram("mata", "atma"))  
print(anagram("mata", "maat"))  
print(anagram("mata", "taam"))  
print(anagram("mata", "tama"))  