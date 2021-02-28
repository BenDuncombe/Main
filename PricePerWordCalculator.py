words_needed = int(input("How many words do you need printed ? "))
if words_needed < 14400:
    words_minute = words_needed / 30
    words_hour = words_minute / 60
    low_rate = words_hour * 21.75
    print ("your labor charge is",(low_rate))
    print ("Your expected labor time is", (words_hour))

else: words_needed > 14440
words_minute = words_needed / 30
words_hour = words_minute / 60
high_rate = words_hour * 25.00
print ("your labor charge is",(high_rate))
print ("Your expected labor time is", (words_hour))

    
    
    
