






def ALI_Convertcost(_input):
    _input = _input.replace('US $', '')
    z = _input.split(' - ')
    
    if len(z) > 1:
        return float(z[0]),float(z[1])
    else:
        try:
            return float(z[0])
        except:
            print('failed to convert: ' + z[0])



