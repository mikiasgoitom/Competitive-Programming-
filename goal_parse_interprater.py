def interpret(command: str) -> str:
    str = ''
    """ i = 0
    while i < (len(command)):
        if( command[i] == "G"):
            str+="G"
        elif command[i] == "(" and command[i+1] == ")":
            str+="o"
            i+=1
            print("result: ", i)
        elif command[i] == "(" and command[i+3] == ")":
            str+='al'
            i+=3
        else:
            return -1
        i += 1 """
    return command.replace('()',"o").replace('(al)','al')
i = "G()(al)"
s = interpret(i)
print(s)