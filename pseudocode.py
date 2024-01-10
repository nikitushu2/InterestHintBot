interest = input("Enter your area of interest: ")

request = send.chatgpt(f"Give me 10 ideas of an activity to do based on my interest: {interest}")

print(request)