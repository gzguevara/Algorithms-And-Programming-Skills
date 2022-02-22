'''

This algorithm computes a list of objects located inside an incapsulated dict. 
Small task, but it took me some time to figure out a clean solution.
'''

my_dict = {
    'a' : 1,
    'b' : 2,
    'c' : {
        'a' : 2,
        'b' : {
            'a': 1,
            'b': {
                'a': 1,
                'b': 2
        }
        }
    },

    'd' : 4
}


def sort_dict(dict, prefix = ''):

    result = []

    for key in dict:

        if type(dict[key]) == int and prefix == '':
            result.append((key, dict[key]))
        
        elif type(dict[key]) == int:
            result.append((prefix + '.' + key, dict[key]))

        elif prefix == '':
            result.extend(sort_dict(dict[key], key))
        
        else:
            result.extend(sort_dict(dict[key], prefix + '.' + key))
        
    return result


sort_dict(my_dict)


def sort_dict2(dict, prefix = ''):

    result = []

    for key in dict:

        if prefix == '':
            prefix_new = key
        else:
            prefix_new = prefix + '.' + key

        if type(dict[key]) == int:
            result.append((prefix_new, dict[key]))
        
        else:
            result.extend(sort_dict(dict[key],prefix_new))
        
    return result


sort_dict2(my_dict)
