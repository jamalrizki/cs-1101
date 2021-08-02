
a = {
    'id': ['1234','date'],
    'series': ['3', 'episode 5'],
    'show': ['my_show', 'part 2']
    }

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for i in val:
          if i not in inverse:
            inverse[i] = [key]
          else:
            inverse[i].append(key)
    return inverse

print('original dict')
print(a)
print('')
print('inverted dict')
print(invert_dict(a))
