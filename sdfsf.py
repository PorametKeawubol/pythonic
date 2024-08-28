def rotate_180(hex_num):
    rotation_map = {
        '0': '0',
        '1': '1',
        '2': '', 
        '3': 'E',  
        '4': '',  
        '5': '', 
        '6': '9',
        '7': '',  
        '8': '8',
        '9': '6',
        'A': '',  
        'b': '9', 
        'C': '', 
        'd': '',  
        'E': '3',  
        'F': ''   
    }
    
    rotated = ''.join(rotation_map.get(ch, '') for ch in reversed(hex_num))  
    return rotated

hex_num = input()
rotated_num = rotate_180(hex_num)
print(len(hex_num)-len(rotated_num))


