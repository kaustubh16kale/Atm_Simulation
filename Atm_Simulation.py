import logging

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="Atm.log",
                    level=logging.INFO)

atm_amount_distribution={500:500,100:500,50:500,20:500,10:500}

def total_amount_display():
    '''
    Function: to display the total amount of notes and value in ATM
    Return : None
    '''
    available_money=0
    print("Amount available in ATM is: ")
    for note,value in atm_amount_distribution.items():
        print(f"{value} notes of {note} Rs = {value*note} Rs")
        available_money+=value*note
    print(f"Total money available in ATM {available_money} Rs")
    return None

def withdraw_money(amount_withdraw):
    '''
    Function to check withdraw conditions and withdraw the money
    Parameter: amount_withdraw : Amount input taken through user
    return : None
    '''
    if amount_withdraw>10000 or amount_withdraw<100:
        logging.warning(f"Amount exceding maximum or minimum withrawal limit {amount_withdraw} Rs")
        print("Unable to withdraw money : Excedding max or min limit of 10000 Rs and 100 Rs")
    elif amount_withdraw%10!=0:
        logging.warning(f"Invalid withdrawable amount should be multiple of 10 : {amount_withdraw} Rs")
        print("Amount should be multiple of 10 to withdraw")
    else:
        notes_withdrawn={}
        total_notes=0
        for value,note in atm_amount_distribution.items():
            note_withdrawn=0
            while note>0 and value<=amount_withdraw:
                amount_withdraw-=value
                note_withdrawn+=1
                total_notes+=1
            if note_withdrawn!=0:
                notes_withdrawn[value]=note_withdrawn
        if total_notes<=40:
            for value,note in notes_withdrawn.items():
                print(f"{value} - {note} notes")
                atm_amount_distribution[value]-=note
            print("Amount withdrawn succesfull")
        else:
            logging.warning(f"Total amount of withdrawable notes exceeded {total_notes} notes")
            print("Unable to withdraw as maximum amount of notes exceeded 40 notes")
        total_amount_display()

def main():
    '''
    Function main()
    Return : None
    '''
    try :
        total_amount_display()
        print("Enter amount to withdraw: ")
        amount_withdraw=int(input())
        withdraw_money(amount_withdraw)
    except Exception as e:
        logging.log(e)


if __name__=="__main__":
    main()