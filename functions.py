def loneliness(type_of_emotion):
    emotevar = "I" + emotion + "you, Luke"
    return emotevar

user_question = input("Do you love me? Yes, No or Maybe: ")
if user_question == "Yes":
    emotion = " love "
    print(loneliness(emotion))

elif user_question == "No":
    emotion = " hate "
    print(loneliness(emotion))

else:
    emotion = " like "
    print(loneliness(emotion))
    




