from langchain.memory import ConversationBufferMemory

memory=ConversationBufferMemory()

def add_to_memory(response,user_input=""):
    if not memory.buffer and user_input=="":
      memory.save_context({"input":"image"},
                          {"ouput":response})
    else:
      memory.save_context({"input":user_input},
                         {"ouput":response})
    

def chat_memory():
  raw_memory=memory.load_memory_variables({})
  return raw_memory
