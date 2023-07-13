import emoji
lan='alias'
emg_input=input('Input: ')
# if '_' in emg_input:
#     lan='en'
print(emoji.emojize('Output: '+emg_input,language=lan))