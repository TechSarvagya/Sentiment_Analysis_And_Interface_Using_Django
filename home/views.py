from django.shortcuts import render
from django.http import request
# from home.SentimentAnalysis import predict

# Create your views
def index(request):
    return render(request,'index.html')
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from englisttohindi.englisttohindi import EngtoHindi
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import dl_translate as dlt
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,r2_score,precision_score,recall_score,f1_score
from sklearn.svm import SVC
from nltk.tokenize import word_tokenize
import seaborn as sns
import os

# %%
with open("Unoff.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    

# %%
lines2=[]
for line in lines:
  if line.find("https://")!=-1 or ":" not in line:
    lines.remove(line)
  splitline=line.split("-")
  if(len(splitline)>=2):
   lines2.append(splitline[1])
  else:
   lines2.append(splitline[0])
 # line.replace("+91 ##### #####:","")
  #line.replace("##### JIMS","")
#for line in lines:
#    re.search
lines3=[]
for line in lines2:
  if(line.find("#:")!=-1):
     lines3.append(line.split(":")[1])
#for line in lines3:
#    line=line.replace("\n","")

# %%
lines3=[i for i in lines3 if len(i)>=20]
lines3=random.choices(lines3,k=500)

# %%
lines4=[]
translator=Translator()
le=np.linspace(0,len(lines3),20,dtype='int16').tolist()

# %%
def translate(l1,l2):
 try:
  for i in range(l1,l2):
    res=translator.translate(lines3[i],src='hindi',dest='english').text
    lines4.append(res)
 except Exception:
    translate(l1,l2)
if (os.path.exists("sentiment_data.txt")!=True):
    translate(le[0],le[1])
    print("Done..")
    translate(le[1],le[2])
    print("Done..")
    translate(le[2],le[3])
    print("Done..")
    translate(le[3],le[4])
    print("Done..")
    translate(le[4],le[5])
    print("Done..")
    translate(le[5],le[6])
    print("Done..")
    translate(le[6],le[7])
    print("Done..")
    translate(le[7],le[8])
    print("Done..")
    translate(le[8],le[9])
    print("Done..")
    translate(le[9],le[10])
    print("Done..")
    translate(le[10],le[11])
    print("Done..")
    translate(le[11],le[12])
    print("Done..")
    translate(le[12],le[13])
    print("Done..")
    translate(le[13],le[14])
    print("Done..")
    translate(le[14],le[15])
    print("Done..")
    translate(le[15],le[16])
    print("Done..")
    translate(le[16],le[17])
    print("Done..")
    translate(le[17],le[18])
    print("Done..")
    translate(le[18],le[19])
    print("Done..")
    lines4.append(translator.translate('tune mujhe haath kaise lagaaya',src='hindi',dest='english').text)
    lines4.remove('This message was deleted')
    random_whatsapp_messages = [
    "Hey, how are you?",
    "What are your plans for the weekend? 🎉",
    "Did you watch that new movie?",
    "I'm running late, be there in 10 minutes.",
    "Let's catch up soon! ☕️",
    "Check out this funny meme! 😂",
    "Happy birthday!",
    "Are you free for a quick chat? 💬",
    "I'm excited about the weekend!",
    "Can you believe what happened?",
    "Congratulations on your promotion! 🎉👏",
    "Let's plan a movie night.",
    "I miss you!",
    "Let's go shopping this weekend.",
    "What's your favorite song?",
    "Thinking of you! ❤️",
    "Don't forget to RSVP for the event.",
    "Did you see the game last night?",
    "I'm so tired today.",
    "Have a great day!",
    "I'm stuck in traffic, will be there soon.",
    "Thanks for the help!",
    "Let's grab lunch tomorrow.",
    "Remember to call Mom today.",
    "Looking forward to seeing you!",
    "Let's discuss this in person.",
    "I'm so bored right now.",
    "Congratulations on your promotion!",
    "Let's plan a movie night.",
    "Are you still awake?",
    "Let's meet at Starbucks.",
    "Have you tried that new restaurant?",
    "Let's go for a walk.",
    "Can you help me with this problem?",
    "Let me know if you need anything.",
    "How's your pet doing?",
    "Let's go shopping this weekend.",
    "Don't forget to pack your charger.",
    "I miss you!",
    "Let's go shopping this weekend.",
    "What's your favorite song?",
    "Thinking of you! ❤️",
    "Hey, how's it going?",
    "Are you free this weekend?",
    "Did you hear the latest news?",
    "Running late, be there soon!",
    "Could you send me that file?",
    "Let's grab lunch together!",
    "That joke you told was so funny! 😄",
    "Happy birthday! 🎂",
    "How was your vacation?",
    "Can you help me with this problem?",
    "I'll be there in about 15 minutes.",
    "Let's plan a movie night soon!",
    "Do you have any plans for tonight?",
    "Congratulations on your achievement! 🎉",
    "Miss you too!",
    "Thanks for your support!",
    "Have you tried that new restaurant?",
    "Let's schedule a meeting for next week.",
    "Sorry for the late reply.",
    "I'm feeling a bit tired today.",
    "Have a great day ahead!",
    "What's your favorite book genre?",
    "Looking forward to catching up!",
    "Can't wait to see you!",
    "Let's discuss this over coffee.",
    "How's the weather over there?",
    "I'm stuck in traffic right now.",
    "Check your inbox for the details.",
    "Have a fantastic weekend!",
    "Don't forget to call your parents.",
    "I'm really proud of your progress!",
    "Let's meet up later.",
    "Thinking of you! ❤️",
    "Excited for the concert tonight!",
    "Where did you get that amazing shirt?",
    "Let's plan a hike soon.",
    "Did you hear about the new exhibit?",
    "Let's grab dinner tomorrow.",
    "Are you up for a quick call? 📞",
    "Thinking about redecorating my room.",
    "What's the best place to buy groceries?",
    "Just finished reading a great book!",
    "Let's go for a bike ride this weekend.",
    "How's your project going at work?",
    "Trying out a new recipe for dinner tonight.",
    "Have you seen any good movies lately?",
    "Can you believe it's almost September?",
    "Let's visit that new café downtown.",
    "Learning a new language is challenging.",
    "What's your favorite type of music?",
    "Let's plan a beach trip soon.",
    "Do you prefer coffee or tea?",
    "Thinking of taking up photography.",
    "Can you recommend a good TV show?",
    "Let's cook dinner together sometime.",
    "Have you ever tried yoga?",
    "Thinking of starting a garden.",
    "Can't believe how fast this year is going!",
    "Let's watch a documentary tonight.",
    "I'm looking forward to the holidays!",
    "Thinking of adopting a pet soon.",
    "Can you share your workout routine?",
    "Let's organize a game night with friends.",
    "What's your favorite season of the year?",
    "Let's plan a road trip for next month.",
    "How's your day been so far?",
    "Are you attending the conference next week?",
    "Let's go for a walk in the park.",
    "Thinking of learning to play an instrument.",
    "Can you recommend a good restaurant for dinner?",
    "Let's have a picnic by the lake.",
    "How's your family doing?",
    "Are you going to the party on Saturday?",
    "Let's have lunch at that new sushi place.",
    "Thinking about taking up painting.",
    "Can you believe it's already October?",
    "Let's try that new dessert place soon.",
    "How's your weekend shaping up?",
    "Thinking of taking a weekend getaway.",
    "Can you suggest a good movie to watch?",
    "Let's plan a visit to the museum soon.",
    "How's your new apartment coming along?",
    "Thinking of starting a blog.",
    "Can you believe how quickly time flies?",
    "Let's go for a hike in the mountains.",
    "How's your online course going?",
    "Are you interested in going camping?",
    "Let's try a new recipe together.",
    "How's your favorite sports team doing?",
    "Are you free for coffee later this afternoon?",
    "Let's plan a day at the beach next weekend.",
    "How's your week been so far?",
    "Are you joining us for the barbecue on Sunday?",
    "Let's meet up for drinks this evening.",
    "How's your new hobby going?",
    "Are you going to the concert next month?",
    "Let's have dinner at that rooftop restaurant.",
    "How's your health these days?",
    "Are you available for a chat right now?",
    "Let's plan a visit to the botanical garden.",
    "How's your side project progressing?",
    "Are you excited about the upcoming holiday?",
    "Let's have a movie marathon this weekend.",
    "How's your morning routine working out?",
    "Are you coming to the book club meeting?",
    "Let's plan a day trip to the nearby town.",
    "How's your recent book recommendation?",
    "Are you up for a game of tennis this weekend?",
    "Let's have brunch at that trendy café.",
    "How's your new year's resolution going?",
    "Are you attending the workshop next week?",
    "Let's go for a bike ride in the park.",
    "How's your garden growing this season?",
    "Are you ready for the big presentation?",
    "Let's try that new ice cream place soon.",
    "How's your pet adapting to the new home?",
    "Are you interested in joining the photography club?",
    "Let's plan a visit to the farmer's market.",
    "How's your online course going so far?",
    "Are you going to the music festival next month?",
    "Let's have a game night with board games.",
    "How's your home renovation project going?",
    "Are you looking forward to the family reunion?",
    "Let's try a new workout routine together.",
    "How's your progress on the fitness challenge?",
    "Are you planning any trips for the holidays?",
    "Let's visit that new art gallery downtown.",
    "How's your new business venture shaping up?",
    "Are you going to the theater play next week?",
    "Let's have a movie night with popcorn.",
    "How's your morning routine going these days?",
    "Are you attending the workshop on Friday?",
    "Let's go for a run in the park.",
    "How's your diet and exercise plan going?",
    "Are you ready for the upcoming exams?",
    "Let's have dinner at that new Italian place.",
    "How's your latest DIY project coming along?",
    "Are you excited about the summer vacation?",
    "Let's plan a weekend getaway to the beach.",
    "How's your meditation practice going?",
    "Are you going to the comic convention next month?",
    "Let's have a picnic in the park this weekend.",
    "How's your progress on learning to play the guitar?",
    "Are you interested in volunteering for the charity event?",
    "Let's try that new restaurant in town soon.",
    "How's your new painting hobby coming along?",
    "Are you going to the annual company party?",
    "Let's have a barbecue party in the backyard.",
    "How's your progress on writing the novel?",
    "Are you excited about the upcoming concert?",
    "Let's go for a hike in the mountains this weekend.",
    "How's your latest knitting project going?",
    "Are you attending the workshop next month?",
    "Let's have brunch at that cute café.",
    "How's your progress on the home renovation?",
    "Are you ready for the beach vacation?",
    "Let's try that new coffee shop downtown.",
    "How's your progress on the language learning?",
    "Are you going to the art exhibition next week?",
    "Let's have a movie night with popcorn and drinks.",
    "How's your progress on the photography project?",
    "Are you interested in going to the dance performance?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you looking forward to the weekend getaway?",
    "Let's have dinner at that new seafood restaurant.",
    "How's your progress on the meditation practice?",
    "Are you excited about the upcoming festival?",
    "Let's go for a bike ride in the park this weekend.",
    "How's your progress on the knitting project?",
    "Are you going to the workshop on Friday?",
    "Let's try that new dessert place in town.",
    "How's your progress on the DIY project?",
    "Are you interested in going to the theater play?",
    "Let's have a picnic by the lake next weekend.",
    "How's your progress on writing the novel?",
    "Are you attending the annual company party?",
    "Let's plan a barbecue party in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you ready for the beach vacation?",
    "Let's try that new restaurant near the office.",
    "How's your progress on learning the language?",
    "Are you going to the charity event next month?",
    "Let's have a movie night with popcorn and drinks.",
    "How's your progress on the photography project?",
    "Are you looking forward to the dance performance?",
    "Let's plan a day trip to the nearby national park.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's have dinner at that new Thai restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the music festival?",
    "Let's go for a hike in the mountains next weekend.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop next month?",
    "Let's try that new gelato place in town.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition next week?",
    "Let's have a picnic at the beach this weekend.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place downtown.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?",
    "Let's go for a hike in the mountains.",
    "How's your progress on the knitting project?",
    "Are you attending the workshop?",
    "Let's try that new coffee shop.",
    "How's your progress on the DIY project?",
    "Are you going to the art exhibition?",
    "Let's have a picnic by the lake.",
    "How's your progress on writing the novel?",
    "Are you ready for the company party?",
    "Let's plan a barbecue in the backyard.",
    "How's your progress on the painting hobby?",
    "Are you excited about the beach vacation?",
    "Let's try that new sushi place.",
    "How's your progress on learning the language?",
    "Are you attending the charity event?",
    "Let's have a movie night with friends.",
    "How's your progress on the photography project?",
    "Are you looking forward to the theater play?",
    "Let's plan a day trip to the countryside.",
    "How's your progress on the fitness challenge?",
    "Are you excited about the weekend getaway?",
    "Let's try that new Italian restaurant.",
    "How's your progress on the meditation practice?",
    "Are you interested in going to the concert?"
     ]
    lines4.extend(random_whatsapp_messages)

# %%
lines4

# %%
if(os.path.exists("sentiment_data.txt")!=True):  
 with open("sentiment_data.txt","w",encoding="utf-8") as f:
    for line in lines4:
      f.write(f'{line}')
      f.write("\n")

# %%
with open("sentiment_data.txt","r",encoding="utf-8") as f:
      lines5=f.readlines()
for i in range(len(lines5)):
  lines5[i]=lines5[i][:len(lines5[i])-1]


# %%
negative_sentences = [
    "I don't like this place.",
    "She never completes her assignments on time.",
    "The food here is not good.",
    "He didn't pass the exam.",
    "I can't believe you did that.",
    "They won't be joining us tonight.",
    "I'm not feeling well today.",
    "This project will never get finished.",
    "You shouldn't have done that.",
    "The weather isn't looking good for tomorrow.",
    "I'm not interested in your excuses.",
    "They don't appreciate my work.",
    "He never listens to me.",
    "I can't find my keys anywhere.",
    "The service here is terrible.",
    "This isn't what I ordered.",
    "I'm not happy with the results.",
    "We can't go on vacation this year.",
    "She didn't show up to the meeting.",
    "I don't understand this topic.",
    "The computer isn't working again.",
    "I can't believe we lost the game.",
    "There are no available seats.",
    "You didn't follow the instructions.",
    "This is not acceptable.",
    "They haven't replied to my email.",
    "He doesn't care about the project.",
    "I can't remember where I parked.",
    "The internet is down again.",
    "This movie is not interesting.",
    "I don't have enough money for this.",
    "We didn't make the deadline.",
    "She doesn't trust anyone.",
    "He hasn't been honest with us.",
    "This product is defective.",
    "I can't get a signal here.",
    "The store is always out of stock.",
    "They never offer any discounts.",
    "I don't want to go to the party.",
    "He didn't come home last night.",
    "This isn't going to work.",
    "I can't solve this problem.",
    "We haven't made any progress.",
    "She won't answer her phone.",
    "I'm not in the mood for this.",
    "He doesn't respect my opinion.",
    "This place is always crowded.",
    "I can't get comfortable in this chair.",
    "The music is too loud here.",
    "I don't agree with your decision.",
    "They aren't taking this seriously.",
    "We didn't get the contract.",
    "She never helps with the chores.",
    "He won't admit his mistake.",
    "I can't believe it's raining again.",
    "This situation is out of control.",
    "I don't like how this is going.",
    "They don't understand my point of view.",
    "He isn't qualified for the job.",
    "I can't deal with this right now.",
    "We aren't prepared for the test.",
    "She doesn't appreciate my efforts.",
    "He won't listen to reason.",
    "I can't stand this heat.",
    "The event was poorly organized.",
    "They haven't fixed the issue yet.",
    "I don't want to talk about it.",
    "He doesn't deserve this award.",
    "I can't accept this offer.",
    "We aren't going to make it on time.",
    "She doesn't follow the rules.",
    "He hasn't apologized yet.",
    "I can't wait to leave.",
    "This plan isn't feasible.",
    "I don't like the new policy.",
    "They don't care about our concerns.",
    "He isn't taking responsibility.",
    "I can't finish this alone.",
    "We aren't allowed to go there.",
    "She didn't inform us in advance.",
    "He doesn't remember anything.",
    "I can't sleep with all this noise.",
    "The instructions aren't clear.",
    "They haven't updated the software.",
    "I don't feel like doing anything.",
    "He won't stop complaining.",
    "This isn't what I expected.",
    "I can't get through to customer service.",
    "We didn't receive the package.",
    "She doesn't take her job seriously.",
    "He won't change his mind.",
    "I can't find a good restaurant nearby.",
    "The printer isn't working again.",
    "They don't provide good customer service.",
    "I don't like how they treated us.",
    "He hasn't finished his work yet.",
    "I can't believe she said that.",
    "We aren't ready for the presentation."
    "I hate you",
    "Get lost from here",
    "Don't ever talk to me",
    "I am angry",
    "You are a traitor"
]

# %%
lines5.extend(negative_sentences)

# %%
more_word_sent = [
    "abandon", "abandoned", "abandoning", "abandonment", "abate", "abated", 
    "abates", "abating", "abhor", "abhored", "abhors", "abhorrence", 
    "abhorrent", "abject", "abjectly", "abjectness", "abnormal", 
    "abnormally", "abrasive", "abrupt", "abruptly", "abruptness", 
    "abscond", "absconded", "absconding", "absentee", "absent", "absently", 
    "absentminded", "absolve", "absolved", "absolves", "absolving", 
    "abstinence", "abstinent", "absurd", "absurdly", "absurdity", 
    "abusive", "abusively", "abuses", "accuse", "accused", "accuses", 
    "accusing", "ache", "ached", "aches", "aching", "acrimonious", 
    "acrimoniously", "admonish", "admonished", "admonishes", "admonishing", 
    "adverse", "adversely", "adversity", "afflict", "afflicted", 
    "afflicting", "affliction", "aggravate", "aggravated", "aggravates", 
    "aggravating", "aggrieved", "aggrieve", "aggrieves", "aggrieving", 
    "angry", "angrily", "annoy", "annoyed", "annoying", "anxiety", 
    "anxious", "anxiously", "appalling", "appallingly", "arbitrary", 
    "arbitrariness", "arduous", "arduousness", "argue", "argued", 
    "argues", "arguing", "arrogant", "arrogantly", "atrocity", "awful", 
    "bad", "badly", "baffle", "baffled", "baffles", "baffling", 
    "barbaric", "barbarically", "belittle", "belittled", "belittles", 
    "belittling", "beneath", "bizarre", "bizarrely", "blame", "blamed", 
    "blames", "blaming", "blunder", "blundered", "blundering", "blunders", 
    "bother", "bothered", "bothers", "bothering", "brutal", "brutally", 
    "brutality", "callous", "callously", "callousness", "cavort", 
    "cavorted", "cavorting", "chaotic", "chaotically", "clumsy", 
    "clumsily", "clumsiness", "coarse", "coarsely", "coarseness", 
    "condemn", "condemned", "condemning", "conflict", "conflicted", 
    "conflicting", "conflictual", "contrary", "contrarily", "contrariness", 
    "corrupt", "corrupted", "corrupting", "corruption", "costly", 
    "crass", "crassly", "crassness", "critical", "critically", 
    "criticism", "culpable", "culpably", "cynical", "cynically", 
    "damage", "damaged", "damages", "damaging", "dark", "darken", 
    "darkened", "darkens", "darkening", "difficult", "difficultly", 
    "dilemma", "dilemmatic", "dire", "disastrous", "discomfort", 
    "discontent", "discontented", "discord", "discordant", "discrepancy", 
    "disease", "dismal", "dismally", "dismay", "dismayed", "dismaying", 
    "displeased", "displeasing", "dissension", "distress", "distressed", 
    "distressing", "doubtful", "doubtfully", "dreadful", "drearily", 
    "drift", "drifted", "drifting", "dull", "dully", "dullness", 
    "dysfunction", "embarrass", "embarrassed", "embarrassing", "enigma", 
    "envious", "enviously", "erratic", "erratically", "exasperate", 
    "exasperated", "exasperates", "exasperating", "failing", 
    "falter", "faltered", "faltering", "false", "falsely", 
    "falsify", "falsified", "falsifies", "falsifying", "fearful", 
    "fearfully", "feeble", "feebly", "flawed", "foolish", "foolishly", 
    "fragile", "fragility", "frantic", "frantically", "frustrate", 
    "frustrated", "frustrates", "frustrating", "fuming", "furious", 
    "furiously", "gloomy", "gloomily", "grievance", "grievances", 
    "grievous", "grievously", "guilty", "guiltier", "guiltiest", 
    "guiltiness", "harsh", "harshly", "harshness", "hasty", 
    "hastily", "hasten", "hastened", "hastens", "hastening", "hazard", 
    "hazarded", "hazarding", "hinder", "hindered", "hindering", 
    "hostile", "hostilely", "hostility", "hurt", "hurting", 
    "hysterical", "hysterically", "impair", "impaired", "impairs", 
    "impatience", "imperfect", "imperfectly", "impose", "imposed", 
    "imposes", "imposing", "ineffective", "ineffectively", "inferior", 
    "inhibit", "inhibited", "inhibiting", "inhibition", "insidious", 
    "insidiously", "instability", "intolerant", "irate", "irately", 
    "irritate", "irritated", "irritates", "irritating", "jeopardize", 
    "jeopardized", "jeopardizes", "jeopardizing", "jittery", "jumpy", 
    "misery", "miserable", "miserably", "mistake", "mistaken", 
    "mistakes", "misunderstood", "misuse", "misused", "misuses", 
    "misusing", "mourn", "mourned", "mourning", "negligent", "nervous", 
    "nervously", "noisome", "numb", "numbness", "obnoxious", 
    "obscure", "obscured", "obscures", "obscuring", "offensive", 
    "offensively", "offensiveness", "oppressive", "oppressively", 
    "outrage", "outraged", "outrages", "outraging", "painful", 
    "painfully", "pessimistic", "pessimistically", "problematic", 
    "quarrel", "quarreled", "quarreling", "questionable", "rage", 
    "raged", "rages", "raging", "reprehensible", "resent", "resented", 
    "resenting", "resentment", "risky", "rough", "sabotage", 
    "sabotaged", "sabotages", "sabotaging", "scandalous", "screech", 
    "screeching", "shady", "shame", "shamed", "shameful", "shamefully", 
    "shocking", "shockingly", "sinister", "sneaky", "sorrowful", 
    "sorrowfully", "stubborn", "stubbornly", "suspicious", "suspiciously", 
    "tainted", "terrible", "terribly", "toxic", "tragedy", "troublesome", 
    "unacceptable", "unacceptably", "unavailable", "unbearable", 
    "unbelievable", "uncaring", "uncertain", "uncivil", "unclean", 
    "unclear", "uncomfortable", "uncomfortablely", "uncooperative", 
    "uncouth", "undecided", "undefined", "undependable", "underdog", 
    "underestimate", "underpaid", "underpowered", "undersized", 
    "undesirable", "undetermined", "undignified", "undone", "unease", 
    "uneasily", "uneasiness", "uneasy", "uneconomical", "unemployed", 
    "unequal", "unethical", "uneven", "uneventful", "unexpected", 
    "unexpectedly", "unexplained", "unfairly", "unfaithful", 
    "unfamiliar", "unfavorable", "unfeeling", "unfinished", "unfit", 
    "unforeseen", "unforgiving", "unfortunate", "unfortunately", 
    "unfounded", "unfriendly", "unfulfilled", "unfunded", "ungovernable", 
    "ungrateful", "unhappy", "unhealthy", "unhelpful", "unimaginable", 
    "unimportant", "uninformed", "uninsured", "unintelligible", 
    "unjust", "unjustifiably", "unjustified", "unkind", "unknown", 
    "unlawful", "unleash", "unlikely", "unlucky", "unnatural", 
    "unnecessary", "unwanted", "unwarranted", "unwelcome", "unwell", 
    "unwieldy", "unwilling", "unwise", "unworkable", "unworthy", 
    "unyielding", "upheaval", "uproar", "uproot", "upset", "urgent", 
    "useless", "usurp", "usurper", "utterly", "vagrant", "vague", 
    "vain", "vanity", "vehement", "vengeance", "vengeful", "venom", 
    "venomous", "vent", "vex", "vexation", "vexing", "vibrate", 
    "vibration", "vice", "vicious", "victimize", "vile", "vilify", 
    "villainous", "vindictive", "violate", "violation", "violent", 
    "viper", "virulence", "virus", "vociferous", "volatile", "vomit", 
    "vulgar", "vulnerable", "wack", "wail", "wallow", "wane", 
    "wanton", "warily", "warlike", "warned", "warning", "warp", 
    "warped", "wary", "washed-out", "waste", "wasted", "wasteful", 
    "wasting", "water-down", "wayward", "weak", "weaken", "weaker", 
    "weakness", "weariness", "wearisome", "weary", "wedge", "weed", 
    "weep", "weird", "wheedle", "whimper", "whine", "whining", 
    "whiny", "whips", "whore", "wicked", "wild", "wilt", "wily", 
    "wimpy", "wince", "wobble", "woe", "woebegone", "woeful", 
    "womanizer", "worn", "worried", "worrier", "worries", "worrisome", 
    "worry", "worrying", "worse", "worsen", "worst", "worthless", 
    "wound", "wounds", "wrangle", "wrath", "wreak", "wreck", 
    "wrest", "wrestle", "wretch", "wretched", "wrinkle", "wrinkled", 
    "wrinkles", "wrip", "wripped", "wripping", "writhe", "wrong", 
    "wrongful", "wrongly", "wrought", "yawn", "zap", "zapped", 
    "zaps", "zealot", "zealous", "zealously", "zombie",
    "a+", "abound", "abounds", "abundance", "abundant", "accessible", 
    "acclaim", "acclaimed", "acclamation", "accolade", "accolades", 
    "accommodative", "accomodative", "accomplish", "accomplished", 
    "accomplishment", "accomplishments", "accurate", "accurately", 
    "achievable", "achievement", "achievements", "achievible", 
    "acumen", "adaptable", "adaptive", "adequate", "adjustable", 
    "admirable", "admirably", "admiration", "admire", "admirer", 
    "admiring", "admiringly", "adorable", "adore", "adored", 
    "adorer", "adoring", "adoringly", "adroit", "adroitly", 
    "adulate", "adulation", "adulatory", "advanced", "advantage", 
    "advantageous", "advantageously", "advantages", "adventuresome", 
    "adventurous", "advocate", "advocated", "advocates", "affability", 
    "affable", "affably", "affectation", "affection", "affectionate", 
    "affinity", "affirm", "affirmation", "affirmative", "affluence", 
    "affluent", "afford", "affordable", "afordable", "agile", 
    "agilely", "agility", "agreeable", "agreeableness", "agreeably", 
    "all-around", "alluring", "alluringly", "altruistic", 
    "altruistically", "amaze", "amazed", "amazement", "amazes", 
    "amazing", "amazingly", "ambitious", "ambitiously", "ameliorate", 
    "amenable", "amenity", "amiability", "amiabily", "amiable", 
    "amicability", "amicable", "amicably", "amity", "ample", "amply", 
    "amuse", "amusing", "amusingly", "angel", "angelic", "apotheosis", 
    "appeal", "appealing", "applaud", "appreciable", "appreciate", 
    "appreciated", "appreciates", "appreciative", "appreciatively", 
    "appropriate", "approval", "approve", "ardent", "ardently", 
    "ardor", "articulate", "aspiration", "aspirations", "aspire", 
    "assurance", "assurances", "assure", "assuredly", "assuring", 
    "astonish", "astonished", "astonishing", "astonishingly", 
    "astonishment", "astound", "astounded", "astounding", 
    "astoundingly", "astutely", "attentive", "attraction", 
    "attractive", "attractively", "attune", "audible", "audibly", 
    "auspicious", "authentic", "authoritative", "autonomous", 
    "available", "aver", "avid", "avidly", "award", "awarded", 
    "awards", "awe", "awed", "awesome", "awesomely", "awesomeness", 
    "awestruck", "awsome", "backbone", "balanced", "bargain", 
    "beauteous", "beautiful", "beautifullly", "beautifully", 
    "beautify", "beauty", "beckon", "beckoned", "beckoning", 
    "beckons", "believable", "believeable", "beloved", "benefactor", 
    "beneficent", "beneficial", "beneficially", "beneficiary", 
    "benefit", "benefits", "benevolence", "benevolent", "benifits", 
    "best", "best-known", "best-performing", "best-selling", "better", 
    "better-known", "better-than-expected", "beutifully", "blameless", 
    "bless", "blessing", "bliss", "blissful", "blissfully", "blithe", 
    "blockbuster", "bloom", "blossom", "bolster", "bonny", "bonus", 
    "bonuses", "boom", "booming", "boost", "boundless", "bountiful", 
    "brainiest", "brainy", "brand-new", "brave", "bravery", "bravo", 
    "breakthrough", "breakthroughs", "breathlessness", "breathtaking", 
    "breathtakingly", "breeze", "bright", "brighten", "brighter", 
    "brightest", "brilliance", "brilliances", "brilliant", 
    "brilliantly", "brisk", "brotherly", "bullish", "buoyant", 
    "cajole", "calm", "calming", "calmness", "capability", "capable", 
    "capably", "captivate", "captivating", "carefree", "cashback", 
    "cashbacks", "catchy", "celebrate", "celebrated", "celebration", 
    "celebratory", "champ", "champion", "charisma", "charismatic", 
    "charitable", "charm", "charming", "charmingly", "chaste", 
    "cheaper", "cheapest", "cheer", "cheerful", "cheery", "cherish", 
    "cherished", "cherub", "chic", "chivalrous", "chivalry", 
    "civility", "civilize", "clarity", "classic", "classy", "clean", 
    "cleaner", "cleanest", "cleanliness", "cleanly", "clear", 
    "clear-cut", "cleared", "clearer", "clearly", "clears", "clever", 
    "cleverly", "cohere", "coherence", "coherent", "cohesive", 
    "colorful", "comely", "comfort", "comfortable", "comfortably", 
    "comforting", "comfy", "commend", "commendable", "commendably", 
    "commitment", "commodious", "compact", "compactly", "compassion", 
    "compassionate", "compatible", "competitive", "complement", 
    "complementary", "complemented", "complements", "compliant", 
    "compliment", "complimentary", "comprehensive", "conciliate", 
    "conciliatory", "concise", "confidence", "confident", 
    "congenial", "congratulate", "congratulation", "congratulations", 
    "congratulatory", "conscientious", "considerate", "consistent", 
    "consistently", "constructive", "consummate", "contentment", 
    "continuity", "contrasty", "contribution", "convenience", 
    "convenient", "conveniently", "convince", "convincing", 
    "convincingly", "cool", "coolest", "cooperative", "cooperatively", 
    "cornerstone", "correct", "correctly", "cost-effective", 
    "cost-saving", "counter-attack", "counter-attacks", "courage", 
    "courageous", "courageously", "craftsmanship", "creative", 
    "creativity", "cultivated", "cultivates", "cultivating", 
    "cultivation", "cultured", "dazzle", "dazzled", "dazzling", 
    "dedicated", "dedication", "deft", "deftly", "delight", 
    "delighted", "delighting", "delightful", "delightfully", 
    "dependable", "deserved", "deserving", "diligent", "diligently", 
    "distinguished", "diverse", "diversify", "diversified", "diversity", 
    "doctrinal", "dominate", "dominated", "dominates", "dominatrix", 
    "dominatory", "dreamy", "durable", "dynamic", "eager", "eagerly", 
    "easy", "easy-to-use", "elegant", "elegantly", "elevate", 
    "elevated", "elite", "endearing", "energetic", "engage", 
    "engaging", "enlighten", "enlightened", "enlightening", 
    "enticing", "enticingly", "enviable", "envision", "essential", 
    "ethereal", "euphoric", "excellent", "excellently", "exemplary", 
    "excels", "exciting", "excitement", "exhilarating", 
    "exhilaratingly", "extraordinary", "fabulous", "fascinate", 
    "fascinated", "fascinating", "fascinatingly", "fantastic", 
    "fantastically", "favorable", "favourable", "favourably", 
    "flourish", "flourished", "flourishing", "fortunate", 
    "fortuitous", "friendly", "fun", "genuine", "gifted", "glad", 
    "gleaming", "glorious", "glow", "glowing", "good", "grace", 
    "graceful", "gracefully", "grateful", "great", "greatest", 
    "groundbreaking", "guarantee", "guaranteed", "guaranteeing", 
    "happy", "harmonious", "heartfelt", "helpful", "honest", 
    "honorable", "honorary", "hopeful", "illuminate", "illuminating", 
    "illuminated", "incredible", "incredibly", "invaluable", 
    "inspired", "inspiring", "innovative", "inquisitive", 
    "insightful", "intelligent", "interesting", "intriguing", 
    "invincible", "joyful", "joyous", "judicious", "kind", 
    "kind-hearted", "knowledgeable", "laudable", "lively", 
    "logical", "lovable", "lovely", "magnificent", "masterful", 
    "memorable", "motivated", "motivating", "outstanding", 
    "passionate", "patient", "perceptive", "perfect", "perfection", 
    "phenomenal", "pleasing", "powerful", "proactive", "proficient", 
    "remarkable", "reliable", "resourceful", "respectable", 
    "responsible", "skilled", "smart", "spectacular", "stellar", 
    "successful", "talented", "terrific", "thoughtful", "top-notch", 
    "trustworthy", "unique", "valuable", "versatile", "vibrant", 
    "vivacious", "well-deserved", "wonderful", "worthy", "zestful",
    "I am feeling great today!",                  # Positive sentence
    "The weather is absolutely beautiful.",       # Positive sentence
    "I just got a promotion at work.",            # Positive sentence
    "I'm so proud of my achievements.",           # Positive sentence
    "This meal is delicious and satisfying.",     # Positive sentence
    "I had a wonderful time with my family.",     # Positive sentence
    "The concert was fantastic and fun.",         # Positive sentence
    "I love spending time with my friends.",      # Positive sentence
    "I received a heartfelt compliment.",         # Positive sentence
    "I feel so motivated and inspired.",          # Positive sentence
    "I am grateful for my good health.",          # Positive sentence
    "I had a productive day at work.",            # Positive sentence
    "The vacation was relaxing and enjoyable.",   # Positive sentence
    "I accomplished my goals for the week.",      # Positive sentence
    "The book I'm reading is fascinating.",       # Positive sentence
    "I feel a deep sense of happiness.",          # Positive sentence
    "I successfully completed the project.",      # Positive sentence
    "The new movie was thrilling and entertaining.",# Positive sentence
    "I feel a strong sense of community.",        # Positive sentence
    "The flowers in the garden are blooming beautifully.", # Positive sentence
    "I am excited about the future.",             # Positive sentence
    "I received praise from my boss.",            # Positive sentence
    "I am learning new skills every day.",        # Positive sentence
    "I feel content and at peace.",               # Positive sentence
    "My hard work is paying off.",                # Positive sentence
    "I am surrounded by love and support.",       # Positive sentence
    "I enjoy my hobbies and interests.",          # Positive sentence
    "I feel confident in my abilities.",          # Positive sentence
    "I am making progress towards my goals.",     # Positive sentence
    "I have a positive outlook on life.",         # Positive sentence
    "I appreciate the little things in life.",    # Positive sentence
    "I feel energized and refreshed.",            # Positive sentence
    "I am grateful for the opportunities I have.",# Positive sentence
    "I feel a sense of accomplishment.",          # Positive sentence
    "I am happy with my relationships.",          # Positive sentence
    "I enjoy the work I do.",                     # Positive sentence
    "I am optimistic about the future.",          # Positive sentence
    "I am proud of my progress.",                 # Positive sentence
    "I feel connected to the people around me.",  # Positive sentence
    "I have a lot to be thankful for.",           # Positive sentence
    "I am happy with where I am in life.",        # Positive sentence
    "I feel positive about my journey.",          # Positive sentence
    "I enjoy learning new things.",               # Positive sentence
    "I feel relaxed and at ease.",                # Positive sentence
    "I am excited about my projects.",            # Positive sentence
    "I am surrounded by positive influences.",    # Positive sentence
    "I feel hopeful and inspired.",               # Positive sentence
    "I am proud of who I am.",                    # Positive sentence
    
    "I am feeling very down today.",              # Negative sentence
    "The traffic is horrible and stressful.",     # Negative sentence
    "I failed the test despite studying hard.",   # Negative sentence
    "I'm disappointed with the outcome.",         # Negative sentence
    "This situation is frustrating and unfair.",  # Negative sentence
    "I had an argument with my best friend.",     # Negative sentence
    "The weather is gloomy and depressing.",      # Negative sentence
    "I lost my wallet and feel stressed.",        # Negative sentence
    "I didn't get the job I wanted.",             # Negative sentence
    "I feel overwhelmed by my responsibilities.", # Negative sentence
    "I'm unhappy with my current situation.",     # Negative sentence
    "The news today is very upsetting.",          # Negative sentence
    "I am struggling with my mental health.",     # Negative sentence
    "I feel lonely and isolated.",                # Negative sentence
    "I made a mistake and feel embarrassed.",     # Negative sentence
    "I am dealing with a lot of stress at work.", # Negative sentence
    "I received some bad news from a friend.",    # Negative sentence
    "I am unhappy with my appearance.",           # Negative sentence
    "The movie I watched was disappointing.",     # Negative sentence
    "I feel a sense of hopelessness.",            # Negative sentence
    "I am frustrated with my progress.",          # Negative sentence
    "I feel like I'm not good enough.",           # Negative sentence
    "I am worried about my future.",              # Negative sentence
    "I feel stuck in my current situation.",      # Negative sentence
    "I am unhappy with my job.",                  # Negative sentence
    "I am feeling anxious and nervous.",          # Negative sentence
    "I feel disconnected from others.",           # Negative sentence
    "I am upset about recent events.",            # Negative sentence
    "I feel like I'm failing.",                   # Negative sentence
    "I am dealing with a lot of uncertainty.",    # Negative sentence
    "I feel like I'm not making progress.",       # Negative sentence
    "I am unhappy with my living situation.",     # Negative sentence
    "I feel like I'm under a lot of pressure.",   # Negative sentence
    "I am not satisfied with my achievements.",   # Negative sentence
    "I feel like I'm missing out.",               # Negative sentence
    "I am struggling to stay positive.",          # Negative sentence
    "I feel like I'm not being heard.",           # Negative sentence
    "I am dealing with a lot of negativity.",     # Negative sentence
    "I feel like I'm not in control.",            # Negative sentence
    "I am unhappy with my personal life.",        # Negative sentence
    "I feel like I'm constantly stressed.",       # Negative sentence
    "I am struggling to find motivation.",        # Negative sentence
    "I feel like I'm always tired.",              # Negative sentence
    "I am feeling very insecure.",                # Negative sentence
    "I feel like I'm not appreciated.",           # Negative sentence
    "I am unhappy with my financial situation.",  # Negative sentence
    "I feel like I'm always behind.",             # Negative sentence
    "I am dealing with a lot of disappointment.", # Negative sentence
    "I feel like I'm not living up to my potential.", # Negative sentence
    "I am struggling to find balance.",           # Negative sentence
    "I feel like I'm always busy.",               # Negative sentence
    "I am unhappy with my health.",               # Negative sentence
]


# %%
print(len(more_word_sent))

# %%
more_words=random.choices(more_word_sent,k=1000)
lines5.extend(more_words)

# %%
len(lines5)

# %%


# %%
for line in lines5:
    if '#' in line:
        lines5.remove(line)
    if 'This message was deleted' in line:
        lines5.remove(line)
len(lines5)

# %%


# %%
df=pd.DataFrame(lines5,columns=["Text"])
df

# %%
sentiment=SentimentIntensityAnalyzer()

# %%
df["Positive"]=[sentiment.polarity_scores(i)['pos'] for i in df['Text']]
df["Negative"]=[sentiment.polarity_scores(i)['neg'] for i in df['Text']]

# %%
df_1=pd.DataFrame()
df_1['Text']=df['Text']
df_1['Sentiment']=[2 if df.iloc[i,1]>df.iloc[i,2] else 1 if df.iloc[i,1]==df.iloc[i,2] else 0 for i in df.index]

# %%
np.random.seed(0)
df_train,df_test=train_test_split(df_1,train_size=0.7,test_size=0.3,random_state=100)
df_train.reset_index(inplace=True)
df_train.drop('index',inplace=True,axis=1)
df_test.reset_index(inplace=True)
df_test.drop('index',inplace=True,axis=1)
df_train

# %%
vectorizer=TfidfVectorizer(strip_accents=None,lowercase=False,preprocessor=None)

# %%
y_train= df_train.pop('Sentiment')
X_train=vectorizer.fit_transform(df_train["Text"])
y_test= df_test.pop('Sentiment')
X_test=vectorizer.transform(df_test["Text"])

# %%

# %%
logreg=LogisticRegression()
logreg.fit(X_train,y_train)

# %%
y_pred=logreg.predict(X_train)

# %%
accuracy_score(y_train,y_pred)

# %%
print(classification_report(y_train,y_pred))

# %%
cm=confusion_matrix(y_train,y_pred)

# %%
plt.figure(figsize=(13,8))
sns.heatmap(cm,cmap='YlOrBr',annot=True, yticklabels=['Negative','Neutral','Positive'],xticklabels=['Negative','Neutral','Positive'])
plt.xlabel("Predicted", fontsize=20)
plt.ylabel("Actual",fontsize=20)
plt.show()

# %%
y_test_pred=logreg.predict(X_test)

# %%
accuracy_score(y_test,y_test_pred)

# %%
tree=DecisionTreeClassifier(max_depth=60,min_samples_leaf=1)

# %%
tree.fit(X_train,y_train)

# %%
y_pred=tree.predict(X_train)

# %%
accuracy_score(y_train,y_pred)

# %%
y_test_pred=tree.predict(X_test)
accuracy_score(y_test,y_test_pred)

# %%
svm=SVC(kernel='linear',C=2,gamma=0.4)
svm.fit(X_train,y_train)
y_pred=svm.predict(X_train)
y_test_pred=svm.predict(X_test)
#We choose the svm model
acc=accuracy_score(y_train,y_pred)
ps=precision_score(y_train,y_pred,average=None)
r=recall_score(y_train,y_pred,average=None)
print(f"Accuracy:{acc}\nPrecision(Positive, Neutral, Negative):{ps}\nRecall(Positive, Neutral, Negative):{r}" )
print(f"f1_score(Positive, Neutral, Negative):{f1_score(y_train,y_pred,average=None)}")

# %%
y_test_pred=svm.predict(X_test)
acc=accuracy_score(y_test,y_test_pred)
ps=precision_score(y_test,y_test_pred,average=None)
r=recall_score(y_test,y_test_pred,average=None)
print(f"Test Accuracy:{acc}\nTest Precision(Positive, Neutral, Negative):{ps}\nTest Recall(Positive, Neutral, Negative):{r}" )
print(f"Test f1_score(Positive, Neutral, Negative):{f1_score(y_test,y_test_pred,average=None)}")

# %%
l1=["i am in love"]
l2=vectorizer.transform(l1)

# %%
y_pred=svm.predict(l2)

# %%
print(y_pred)

# %%
prob1=logreg.predict_proba(l2)
prob2=tree.predict_proba(l2)

# %%
print(prob1)
print(prob2)
   
        







   
def result(request):
    sentence=request.POST.get("sentence")
    y_pred=svm.predict(vectorizer.transform([sentence]))
    if y_pred[0]==0:
        sen="You have said a Negative sentence"
    elif y_pred[0]==1:
        sen="You have said a Neutral sentence"
    else:
        sen="You have said a Positive sentence"
    print("Sentiment:",sen)
    context={
     'sentimnt': sen 
    }
    return render(request,'index.html',context)
