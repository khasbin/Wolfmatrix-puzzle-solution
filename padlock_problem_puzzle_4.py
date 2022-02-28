def checknumbers(number, con, correct_digit, correct_position):
    count_correct_digit = 0
    count_correct_position = 0
    checknumber = str(number).zfill(len(con))
    for i in range(len(con)):
        if checknumber[i] in con:
            count_correct_digit +=1
        if checknumber[i] == con[i]:
            count_correct_position += 1
    if correct_digit == count_correct_digit and correct_position == count_correct_position:
        return True
        
def solution(con1:str, con2:str, con3:str, con4:str, con5:str):
    #con1 -> one digit right but in right place
    #con2 -> one digit right and in wrong place
    #con3 -> two digits correct but in wrong place
    #con4 -> all digits are wrong place
    #con5 -> one digit right but in wrong place
    start = 0
    for number in range(1000):
        if checknumbers(number,con1, 1, 1) and checknumbers(number,con2, 1, 0) and checknumbers(number,con3, 2, 0) and checknumbers(number,con4, 0, 0) and checknumbers(number,con5, 1, 0):
            print(f'The required solution is {str(number).zfill(len(con1))}')
            break

solution("682", "614", "206", "738", "380")
