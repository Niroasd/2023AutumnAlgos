def custom_encoder(dataInput: str):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    data = dataInput.lower()
    positionArray = []
    innerLoops = 0
    
    for x in data:
        if x not in reference_string:
            positionArray.append(-1)
            continue

        for y in reference_string:
            if x != y:
                innerLoops += 1
                continue
            else:
                positionArray.append(innerLoops)
                innerLoops = 0
                break
        
    return positionArray