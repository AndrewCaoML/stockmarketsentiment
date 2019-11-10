import ensemble as sentiment

while True:
    text = input("Enter your phrase: ")

    emo, con = sentiment.score(text)
    
    if emo == "pos":
        emotion = "Positive"
    elif emo == "neg":
        emotion = "Negative"
        
    if con <= 0.3:
        constr = "Slightly Confident"
    elif con > 0.3 and con <= 0.6:
        constr = "Moderately Confident"
    else:
        constr = "Confident"
    
    print("Sentiment:")
    print(emotion)
    print("Confidence Score:")
    print(con)
    print(constr)