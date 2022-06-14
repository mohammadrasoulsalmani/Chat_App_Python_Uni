import pandas as pd
import random
import difflib
from tkinter import *
from tkinter import simpledialog

#read data from csv file
dataset = pd.read_csv("data.csv")
#opening the window
window = Tk()
window.geometry("700x400")
window.title("Deltstack")
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
output_list = Listbox(window, yscrollcommand=scrollbar.set,
                      width=100, bg='azure', font='TkDefaultFont 11')
#list of Inventory
inventory_amount_list = {
    'goosht': 25,
    'sabzi': 55,
    'noshabe': 20,
    'peste' : 20,
    'roghan' : 8,
    'shampo' : 22,
    'dastmal' : 30
}

amount_list = {
    'goosht': 0.0,
    'sabzi': 0.0,
    'noshabe': 0,
    'peste' : 0.0,
    'roghan' : 0,
    'shampo' : 0,
    'dastmal' : 0
}

amount_list_price = {
    'goosht': 150,
    'sabzi': 25,
    'noshabe': 15,
    'peste' : 370,
    'roghan' : 62,
    'shampo' : 28,
    'dastmal' : 12
}


#########################################################################################################################################
#Calculate the cost
def show_sorathesab():
    amount_list_value = list(amount_list.values())
    amount_list_price_value = list(amount_list_price.values())
    sum = 0
    len_list = len(amount_list_value)
    for i in range(len_list):
        sum += amount_list_value[i] * amount_list_price_value[i]
    output_list.insert(END, f'🤖 : sorathesab shama : {sum} Toman')

#########################################################################################################################################
#amount of the goods  in our stock
def inventory_amount():
    list_pass_value = ['Kilo', 'Kilo', 'Ta', 'Kilo' , 'Ta' , 'Ta' , 'Ta']
    k = 0
    for i, j in inventory_amount_list.items():
        if j > 0:
            output_list.insert(END, f'🤖 : {i} : {j} {list_pass_value[k]}')
        k = k + 1
#########################################################################################################################################
#Total cost
def price():
    for i, j in amount_list_price.items():
            output_list.insert(END, f'🤖 : {i} : {j} Toman ')

#########################################################################################################################################
#empty the shopping list after payment
def checkout():
    global amount_list
    amount_list = {
    'goosht': 0.0,
    'sabzi': 0.0,
    'noshabe': 0,
    'peste' : 0.0,
    'roghan' : 0,
    'shampo' : 0,
    'dastmal' : 0
}
    return amount_list

#########################################################################################################################################
#Show the amount of stuff that you bought
def show_the_amount_list():
    list_pass_value = ['Kilo', 'Kilo', 'Ta', 'Kilo' , 'Ta' , 'Ta' , 'Ta']
    k = 0
    l = 0
    for i, j in amount_list.items():
        if j > 0:
            output_list.insert(END, f'🤖 : {i} : {j} {list_pass_value[k]}')
        if j == 0:
            l = l + 1
        k = k + 1
    if l == 7:
        output_list.insert(END, f'🤖 : list shoma khalist !!! ')
        output_list.insert(END, f'🤖 : lotfan aval sefaresh bedidi ')

#########################################################################################################################################
#Add to cart
def add_to_basket(final_answer_key, int_amount):
    int_list_key = inventory_amount_list[final_answer_key]
    if int_list_key < int_amount:
        output_list.insert(END, f'🤖 : megdare vared shode az mojodi bishtare')
    else:
        amount_list[final_answer_key] += int_amount
        inventory_amount_list[final_answer_key] -= int_amount

#########################################################################################################################################
#Respond to the order
def final_answer_list(final_answer, final_answer_key):
    list_answer_amount = simpledialog.askstring(
        "Input", final_answer, parent=window).lower()
    list_answer_amount_list = list(list_answer_amount.split(' '))
    len_list_amount = len(list_answer_amount_list)
    if len_list_amount == 1:
        int_amount = float(list_answer_amount_list[0])
        output_list.insert(END, f'🤖 : safaresh sabt shod!')
        add_to_basket(final_answer_key, int_amount)

    elif len_list_amount <= 0:
        output_list.insert(
            END, f'{list_answer_amount} \n i could not understand "{list_answer_amount}", please ask again:')
        final_answer_list(final_answer)
    else:
        int_amount = float(list_answer_amount_list[0])
        variable_pass = difflib.get_close_matches(
            list_answer_amount_list[1], ['kilo', 'kilogeram', 'kg' , 'ta' , 'adad' , 'done'])
        if len(variable_pass) == 0:
            final_answer_list(final_answer)
        else:
            add_to_basket(final_answer_key, int_amount)
            output_list.insert(END, f'🤖 : safaresh sabt shod!')

#########################################################################################################################################
#checking the type of question
def check_the_answer(final_answer_type,final_answer,final_answer_key):
    if final_answer_type == 3:
        final_answer_list(final_answer, final_answer_key)
    if final_answer_type == 4:
        show_the_amount_list()
    if final_answer_type == 5:
        show_sorathesab()
    if final_answer_type == 6:
        inventory_amount()
    if final_answer_type == 7:
        checkout()
    if final_answer_type == 8:
        price()
    if final_answer_type == 9:
        window.destroy()

#########################################################################################################################################
#Intraction with user
def intdialogbox():
    try:
        message = simpledialog.askstring(
            "Input", "enter your question", parent=window).lower()
        # spliting the dataset
        dataset_for_Question = dataset["Question"]
        # finde the closest answer from dataset
        true_message = difflib.get_close_matches(
            message, dataset_for_Question.values)
        # pick the first answer just for last value
        last_value = true_message[0]
        # getting the index of answers from dataset
        number = dataset.index[dataset['Question'] == last_value].tolist()
        # pick one of the answer's index randomly
        picking_answer = random.choice(number)
        # getting the value of index
        final_answer = dataset.iloc[picking_answer, 1]
        final_answer_type = dataset.iloc[picking_answer, 2]
        final_answer_key = dataset.iloc[picking_answer, 3]
        # checking to see if the final answer is equal to message
        if last_value == message:
            output_list.insert(END, f'{last_value}')
            output_list.insert(END, f'🤖 : {final_answer}')
            check_the_answer(final_answer_type,final_answer,final_answer_key)
        else:
            output_list.insert(END, f'do you mean: {last_value}?')
            output_list.insert(END, f'🤖:{final_answer}.')
            check_the_answer(final_answer_type,final_answer,final_answer_key)


    except IndexError:
        output_list.insert(
            END, f'{message} \n i could not understand "{message}", please ask again:')
        intdialogbox()

    except TypeError:
        output_list.insert(
            END, f'please enter something that i can asnwer you ')

    except UnboundLocalError:
        intdialogbox()


dialog_btn = Button(window, text='ask me', command=intdialogbox)
dialog_btn.pack()
output_list.pack(padx=5, pady=25)
scrollbar.config(command=output_list.yview)

window.mainloop()
