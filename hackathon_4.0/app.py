import streamlit as st
import time as time
from img_preprocess import load_img
from PIL import Image

from memory import chat_memory
from rag_retriving import Recipe_generation
uploadedImage=None
uploaded_file=None
promts = []
from memory import add_to_memory

def main():
    cssCodeExecution() 
    col1,col2=st.columns([1,4])
    col1.markdown("<div class='header'><h1 style=color:darkblue;>GEN AI APP</h1></div>", unsafe_allow_html=True)

    userPromt=st.chat_input(placeholder="Please Enter Your promt")
    # answer = "This is the answer to Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat similique adipisci nobis aliquam, quidem porro exercitationem odio tempore saepe repudiandae placeat. Architecto fuga itaque, velit magnam, alias hic voluptatem optio a ducimus cumque doloremque officia, obcaecati rerum libero! Obcaecati dolore quasi natus dolorum totam debitis accusantium possimus sequi ipsa ipsam, labore impedit, laboriosam veniam sapiente magni velit nobis officia enim illum omnis expedita ratione voluptatum. Eum ipsum, sunt quaerat laudantium harum id quidem blanditiis quo voluptatum a, reiciendis numquam quis facere officia? Dolores nam ullam nisi quod similique, necessitatibus voluptate ipsa eius libero ducimus est atque nemo optio reprehenderit deleniti iusto accusamus? Ad quod, molestiae saepe provident mollitia, sint nesciunt fugiat voluptas sapiente labore officiis possimus, reiciendis cupiditate est ex debitis! Laboriosam modi ut corporis commodi dignissimos quod laborum, quas magni. Laborum pariatur distinctio veniam labore. Debitis id mollitia harum alias minus enim, rem nam dicta incidunt itaque quos commodi dolorum. Voluptas, voluptatem tempora aut iste hic laborum culpa fugit dignissimos quaerat animi nemo veritatis odio adipisci sunt earum nesciunt repudiandae eligendi mollitia. Ullam voluptatem dignissimos quos quaerat iure molestiae facilis ab suscipit aspernatur dolorem, voluptas omnis modi ex quis incidunt blanditiis doloremque repellendus reprehenderit soluta consequatur eius deserunt! Earum ipsam cum corporis impedit? Fugit cum aliquid, officiis odio, fugiat sit ullam quibusdam aspernatur quo unde neque nemo cupiditate asperiores aut ipsum nostrum eveniet dignissimos velit error delectus voluptas laborum. Ipsum minus omnis beatae quibusdam ea quae ullam voluptatem quia cumque id possimus ipsa doloribus temporibus minima harum fugit atque veritatis, officia voluptate voluptates facilis consequatur explicabo inventore! Minus, nobis delectus. Distinctio tempore vel quia, debitis doloremque repudiandae voluptatibus dolorem possimus, officiis praesentium blanditiis incidunt. Incidunt modi numquam, hic ullam laboriosam nihil sequi expedita iure nostrum nulla voluptates ad id reprehenderit exercitationem consequatur officiis voluptas dolor aut veritatis omnis ut beatae. Facere, veniam repellat tempora pariatur explicabo illum ex asperiores nulla excepturi delectus voluptatum, odio nesciunt distinctio temporibus illo officiis. Sed cum vitae aperiam enim quibusdam ea quia odio mollitia ipsam placeat vel quam similique excepturi ipsa minima quisquam inventore, officiis ex saepe blanditiis laborum pariatur reiciendis. Cumque illo velit eius? Aspernatur, corrupti eveniet dignissimos aperiam et dicta facere! Molestias quas vel, aut modi repellat impedit ducimus hic iusto veritatis laudantium dolorum nisi obcaecati dolor ratione inventore eligendi ipsa eaque maxime non possimus voluptatem iure, numquam culpa. Laboriosam esse ea aliquam omnis earum voluptatibus, atque reiciendis porro quasi voluptatem facilis eos aspernatur ex praesentium dolorem harum voluptate sapiente in fuga! Obcaecati consectetur magni pariatur accusamus expedita ex maxime quisquam voluptatum nulla quaerat aperiam cupiditate repudiandae, velit nisi corporis quo fugit aspernatur est dolor voluptates. Quod nam laboriosam omnis similique corporis blanditiis perferendis quam magnam asperiores sint modi numquam beatae, rem vero ratione quis? Ullam, sunt sit accusantium aliquid inventore magni consequatur aut tempora commodi alias aperiam! Sed quidem dolores recusandae atque. Nulla non nihil velit recusandae sapiente cupiditate nisi maiores? Sunt facere explicabo cumque facilis unde quis numquam consequuntur. Molestiae doloremque, voluptatibus accusantium praesentium, dolorem, necessitatibus cupiditate ea similique earum possimus porro. In doloremque provident dignissimos consequatur, aliquid totam voluptate veritatis fuga incidunt nam placeat quas! Quisquam quia ut, dignissimos sequi officia excepturi quo blanditiis minus voluptates atque illo! Nesciunt commodi unde fugiat eum cumque similique maiores reprehenderit? Nobis quis nesciunt voluptatum voluptatem. Quis iure, eaque veniam deserunt facere nesciunt culpa sunt ea hic nostrum ipsa ut omnis possimus voluptatum, nulla minus blanditiis laborum, ex officiis temporibus placeat tenetur perferendis iusto sit. Laboriosam, in, consectetur quod inventore voluptatibus ab error maxime, voluptatem ullam commodi ad nesciunt! Obcaecati eligendi quibusdam aspernatur fugit fuga. Debitis hic temporibus reiciendis quae obcaecati vero doloremque deleniti nihil voluptatibus numquam. Dolore consequatur impedit dolor ab natus aliquid, magni vel harum? Ullam pariatur ut sunt laboriosam non possimus harum nesciunt, odit enim fugit architecto autem voluptates accusantium maxime natus. Temporibus molestias aspernatur libero praesentium distinctio? Officia itaque sint velit magni corrupti et distinctio, sunt ad illum alias nulla architecto ullam quibusdam illo quo ipsam eaque dolorum laboriosam perspiciatis maxime natus doloribus repellat, earum iusto. Quam dignissimos expedita doloremque amet odit dolorum at ex tenetur neque, non eaque assumenda veritatis aliquam harum modi molestias cum eius totam voluptatibus. Labore vitae quisquam laborum cumque facilis repudiandae quam est dolores eveniet consequuntur. Neque assumenda tenetur omnis non, dicta odio sequi eum nemo tempora dolorem dolor inventore sint quidem ut ducimus eaque optio cupiditate nobis architecto corporis unde rem? Harum necessitatibus architecto, beatae odio repellat possimus pariatur excepturi illum doloremque esse, aperiam qui quae ipsam sed modi asperiores in numquam nobis, ducimus distinctio veniam tenetur at debitis delectus. Optio deleniti ab eaque aliquid cupiditate dicta quae est corporis quos adipisci excepturi ex saepe officia veniam exercitationem numquam sed officiis ad cumque, eos in cum nisi atque dolor. Nulla, facere quod iusto error voluptatibus neque aspernatur consequuntur quas harum nobis nesciunt. Quod quaerat mollitia ab dolorem aut asperiores id ipsa aliquid vero voluptates odio tenetur sunt sequi consequatur ratione dignissimos ipsum, recusandae officia? Sint mollitia in deleniti iusto sit architecto ducimus debitis earum necessitatibus optio sunt odio pariatur placeat ut, dolore dolorem labore at eveniet sequi ab saepe quasi quisquam amet inventore. Quos quas officiis, dignissimos perferendis animi quasi neque ratione placeat illo unde laudantium, nulla quae! Nostrum nisi repellendus at ducimus architecto accusantium voluptas placeat, dignissimos aliquid deleniti pariatur ea ipsam, culpa iusto debitis? Impedit obcaecati quisquam veniam perferendis nostrum, eum officia modi eaque qui aspernatur ex maiores. Delectus, accusantium consequuntur ea neque quibusdam mollitia libero rerum inventore eum cum laudantium exercitationem dolorem necessitatibus vero error voluptates quam nesciunt repellat debitis distinctio natus. Voluptatibus eum iusto nemo facere reiciendis quaerat dolores nisi quisquam ipsum perspiciatis sint suscipit amet cum unde, fuga architecto sequi vero quos rerum labore eligendi consectetur harum. Neque dolorum quia voluptatem id, distinctio fuga maxime reprehenderit, labore provident necessitatibus nihil ipsam quo hic, ut quibusdam vero dignissimos soluta illo aliquid assumenda eos deleniti consectetur laudantium sapiente. Consequatur sed ad ratione magni aliquid eveniet saepe qui sit, cupiditate impedit tempore quod! Recusandae delectus sunt nobis nostrum? Pariatur, laborum a.the bold question. It can be much longer and will scroll if it overflows the 300% viewport height."
   

    with st.container():
        for promt in promts:
            for question, solution in promt.items():
                st.markdown(f"<div class='question-container'><div class='text-container'><p class='question'>{question}</p><p>{solution}</p></div></div>", unsafe_allow_html=True)

    selected_option=st.sidebar.selectbox("Choose an Option:",options=["Image", "Multi Module"])
    # Display the selected option
    if selected_option == "Image":
        uploadedImage = st.sidebar.file_uploader("Choose Image",type="jpg")
        imageExtractionProcess(uploadedImage)
        
    elif selected_option == "Multi Module":
        uploaded_file = st.sidebar.file_uploader("Choose a PDF or Doc file:", type=["pdf", "docx"])
        multiModuleRagProcess(uploaded_file)
    if userPromt:
        answer=Recipe_generation(userPromt)
        print("-------------->",userPromt)
        print("-------------->",answer)
        add_to_memory(response=answer,user_input= userPromt)
    st.markdown(chat_memory())



# Function to display Status message as toast on Sidebar
def toastForSidebar(statusMessage):
    toast_message=statusMessage
    time.sleep(1)  # Wait for 1 second
    toast_message.empty()  # Clear the success message

# Function to display Status message as toast on MainScreen
def toastForMainScreen(message):
    toast_message=message
    time.sleep(1)  # Wait for 1 second
    toast_message.empty()  # Clear the success message

def cssCodeExecution():
    st.markdown("""
    <style>
        .header
        {
            background-color: white; /* Light grey background for header */
            padding: 5px;
            color: aqua;
            position: fixed; /* Fix the header to the top */
            top: 0; /* Position it at the top of the viewport */
            width: 100%; /* Make it span the entire width */
            z-index: 5; /* Ensure the header stays on top during scrolling */
        }
        .question-container 
        {
            border-radius: 10px; /* Round corners */
            overflow-y: auto; /* Enable scrolling for content within */
        }
        .question 
        {
            background-color: #e0e0e0; /* Light grey background for question */
            padding: 5px; /* Add some padding for better separation */
            border-radius: 5px; /* Round corners for the question paragraph */
            font-weight: bold; /* Bold text for question */
        }
        .st-emotion-cache-18ni7ap.ezrtsby2
        {
            visibility:hidden;
        }
    </style>
    """,unsafe_allow_html=True)
def imageExtractionProcess(image):
    if image is not None: 
         # Display success message as toast
         toastForSidebar(st.sidebar.success("File uploaded successfully!"))
         st.sidebar.image(image)
             
         img=Image.open(image)
         load_img(img)
        #  st.markdown(chat_memory())


def multiModuleRagProcess(file):  
    if file is not None: 
         # Display success message as toast
         toastForSidebar(st.sidebar.success("File uploaded successfully!"))
    else:
        uploaded_file=None
        

                 
if __name__ == "__main__":
    main()