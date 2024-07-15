
import numpy as np
import pandas as pd
import pickle as p
import openai
from sentence_transformers import SentenceTransformer,util


sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
COMPLETIONS_MODEL = "text-davinci-003"
x = "C:\\Users\\sunny\\BankFAQs.csv"




def convert_to_list(x,i,j):  # get input in list
    df = pd.read_csv(x)
    x = df.iloc[:,i:j]
    sentences = x.values.tolist()
    return sentences

def AnswerFraming(x,y,query):
    prop=y+x+" Or "+query
    openai.api_key = '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'
    z=openai.Completion.create(prompt=prop,temperature=0,max_tokens=300,model=COMPLETIONS_MODEL)["choices"][0]["text"].strip(" \n")
    return(z)

def AnswerFramingX(query):
    prop=query
    openai.api_key = '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'
    z=openai.Completion.create(prompt=prop,temperature=0,max_tokens=300,model=COMPLETIONS_MODEL)["choices"][0]["text"].strip(" \n")
    return(z)

def customer_response(query):
    #show query to other window
    cc_ans=input()
    #show that answer to user window
    query_emb=sbert_model.encode(query)
    q.append(query)
    a.append(cc_ans)
    e.append(query_emb)
    #adding question to database and recompute the embedding
    with open("questions.pkl",'wb') as que:
        p.dump(q,que,protocol=p.HIGHEST_PROTOCOL)
    with open("answers.pkl",'wb') as ans:
        p.dump(a,ans,protocol=p.HIGHEST_PROTOCOL)
    with open("embedding.pkl",'wb') as emb:
        p.dump(e,emb,protocol=p.HIGHEST_PROTOCOL)
    #getting answer to question



questions = convert_to_list(x,0,1)#three dimentions are used lol xd
q=[]
for i in range(len(questions)):
    q.append(questions[i][0])
    
answers=convert_to_list(x,1,2)

a=[]
for i in range(len(questions)):
    a.append(answers[i][0])

e=[]
for i in range(len(questions)):
    e.append(sbert_model.encode(q[i]))

with open("questions.pkl",'wb') as que:
  p.dump(q,que,protocol=p.HIGHEST_PROTOCOL)
with open("answers.pkl",'wb') as ans:
  p.dump(a,ans,protocol=p.HIGHEST_PROTOCOL)
with open("embedding.pkl",'wb') as emb:
  p.dump(e,emb,protocol=p.HIGHEST_PROTOCOL)


def start():  # dialog managment
    with open('questions.pkl','rb') as que:
      q=p.load(que)
    with open('answers.pkl','rb') as ans:
      a=p.load(ans)
    with open('embedding.pkl','rb') as emb:
      e=p.load(emb)


    print("How Can I help you")
    query = input()
    query_emb=sbert_model.encode(query)
    x=[]
    for i in range(len(q)):
      x.append(util.cos_sim(query_emb,e[i]))
    
    cos=[]
    for i in range(len(q)):
      cos.append(float(x[i][0][0]))
    
    y=zip(q,a,cos)
    z=list(y)

    z.sort(key=lambda z: z[2], reverse=True)

    Dict = {}
    top_5q=[]
    top_5a=[]

    i=0
    while(len(Dict)!=5):
      Dict[z[i][0]]=z[i][1]
      i+=1   
    
    for keys,value in Dict.items():
      top_5q.append(keys)
      top_5a.append(value)

    
    for j in range(5):
        print("Do you mean "+top_5q[j])
        che = input()
        che = che.upper()
        if che == 'YES':
            k=AnswerFraming(top_5q[j],top_5a[j],query)
            print(k)
            j+=1
            break
        else:
            continue
    if(j == 4):
        print("Solution:- "+AnswerFramingX(query))
        print("Are you Satisfied")
        x=input()
        x=x.upper()
        if(x=="NO"):
            print("I am out of solution I will convey query to customer care \nPlease provide brief detail about yourself")
            customer_response(query)




start()



