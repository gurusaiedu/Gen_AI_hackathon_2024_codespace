from langchain.memory import ConversationBufferMemory

memory=ConversationBufferMemory()

def add_to_pdf_memory(response,user_input):
    # if not memory.buffer and user_input=="":
    #   memory.save_context({"input":"IMG"},
    #                       {"ouput":response})
    # else:
    memory.save_context({"input":user_input},
                         {"ouput":response})

def pdf_chat_memory():
    r=memory.load_memory_variables({})
    return r
    # return memory.buffer