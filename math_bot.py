#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def process_math_question(user_input):
    user_input = user_input.lower()
    
    match = re.search(r"(\\d+)\\s*([+\\-x*/])\\s*(\\d+)", user_input)
    if not match:
        return "Oops! I can only help with simple math like 2 + 2 or 5 x 3 😊"

    num1 = int(match.group(1))
    operator = match.group(2)
    num2 = int(match.group(3))

    if operator == '+':
        result = num1 + num2
        op_text = "plus"
    elif operator == '-':
        result = num1 - num2
        op_text = "minus"
    elif operator in ['x', '*']:
        result = num1 * num2
        op_text = "times"
    elif operator == '/':
        if num2 == 0:
            return "Oops! Dividing by zero is not allowed 😬"
        result = num1 / num2
        op_text = "divided by"
    else:
        return "Hmm... I didn’t understand that. Try something like 4 + 5."

    return f"Great question! {num1} {op_text} {num2} equals {result} 🎉"

