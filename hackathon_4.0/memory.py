from langchain.memory import ConversationBufferMemory

memory=ConversationBufferMemory()

def add_to_memory(response,user_input=""):
    if not memory.buffer:
      memory.save_context({"input":"IMG"},
                          {"ouput":response})
    else:
      memory.save_context({"input":user_input},
                         {"ouput":response})
    

def chat_memory():
   return memory.buffer

