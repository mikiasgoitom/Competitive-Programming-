def compare(lg_str, sm_str, tot_len):
    while(lg_str !='' and sm_str != ''):
        if(lg_str.find(sm_str) == -1):
            lg_str = lg_str[1:]
            sm_str = sm_str[1:]
        else:
            if(lg_str == sm_str):
                return tot_len - (len(lg_str)+len(sm_str))
            else:
                lg_str = lg_str[1:]         
    return tot_len - (len(lg_str)+len(sm_str))


str1 = input()
str2 = input()

lg_str = ''
sm_str = ''

if(len(str1) > len(str2)):
    lg_str = str1
    sm_str = str2
else:
    lg_str = str2
    sm_str = str1

tot_len = len(lg_str)+len(sm_str)
print(compare(lg_str, sm_str, tot_len))


        