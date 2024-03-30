from ghostai import chat # You can install with "pip install ghostai"

while True: # Creating a forever Loop
    user_input = input('Enter your input : ') # Asking the user for the input


    response = chat("API_KEY_GOES_HERE","chat",user_input) # The API Key can be found at https://api.ghostai.me/getkey

    print(f'AI : {response}') # Printing the AI's Response
