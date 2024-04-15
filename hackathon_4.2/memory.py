from langchain.memory import ConversationBufferMemory

memory=ConversationBufferMemory()

def add_to_memory(response,user_input=""):
    if not memory.buffer and user_input=="":
      memory.save_context({"input":"IMG"},
                          {"ouput":response})
    else:
      memory.save_context({"input":user_input},
                         {"ouput":response})
    

def chat_memory():
  r=memory.load_memory_variables({})
  return r

  # history=r['history']
  # chat_array=history.split("\n")

  # t=0
  # h=""
  # a=""
  # for i in chat_array:
  #   if i.startswith("Human"):
  #     t=1
  #     # h=h+i
  #   elif i.startswith("AI"):
  #     t=2
  #     # a=a+i
  #   if t==1:
  #     h=h+i
  #   elif t==2:
  #     a=a+i

  # a1=a.split("AI:")
  # h1=h.split("Human:")

  # ll=[]
  # for i in range(len(a1)):
  #   if i>0 :
  #     a2="AI:"+a1[i]
  #     h2="Human:"+h1[i]
  #     ll.append(h2)
  #     ll.append(a2)

  # return ll



