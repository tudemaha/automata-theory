from menu.printing import finish_message

def isMember(string, alphabets):
    for char in string:
        if char not in alphabets:
            return False
    
    return True

def isAccepted(lastState, finishState):
    if lastState in finishState: return True
    else: return False
    