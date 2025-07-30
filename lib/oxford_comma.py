def oxford_comma(items):
    if len(items)==1:
        return items[0]
    elif len(items)==2:
        return items[0]+" and "+ items[1]
    else:
        S=", ".join(items[:-1])
        S=S+", and "+items[-1]
        #print(S)
        return S
#oxford_comma(["fiddleheads", "okra", "kohlrabi"])