import streamlit as st
from PIL import Image
import requests
import json

css_style = """
<style>
   .about {
        text-align: justfiy;
        border: 2px solid black;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        margin-top: 20px;
        text-align: justify;
   }

   .grid-container {
        display: grid;
        grid-template-columns: auto auto;
        padding: 15px;
        column-gap: 5px;
        row-gap: 5px;
        border: 2px solid black;
        border-radius: 10px;
   }

   .grid-item {
         text-align: center;
   }

    .img {
        width: 80%;
        height: 250px;
        margin-left: 10px;
        transition: transform 2s;
   }

    .label {
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
   }

    .img:hover {
        transform: scale(1.1);
        
   }

    .img:hover + p {
        margin-top: 10px;
   }

   .link:hover {
         color: red;
   }

</style>
"""
#set css styles
st.markdown(css_style, unsafe_allow_html=True)

def get_prediction_image(image_data, header_data):
  #copy the URL
  url = 'https://yamunainstance1-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/730888e5-b970-4538-998d-af77d7c46a67/classify/iterations/Iteration1/image'
  r = requests.post(url,headers = header_data, data = image_data)
  response = json.loads(r.content)
  print(response)
  return response

def get_prediction_link(link, header_data):
  #copy the endpoint URL
  url = 'https://yamunainstance1-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/730888e5-b970-4538-998d-af77d7c46a67/classify/iterations/Iteration1/url'
  r = requests.post(url,headers = header_data, data = json.dumps(link))
  response = json.loads(r.content)
  print(response)
  return response

subscription_key = '712fb8ca42394295b148d5d78769a25e'#prediction key

#imagine cup
st.title("Hydroponic Lettuce with Deficiency")

#project image
st.image("https://cdn.shopify.com/s/files/1/2224/2977/files/135115781_m.jpg?v=1643602660", caption = "Lettuces")

#set the sidebar
with st.sidebar:
   #title of the webpage
   st.title("Hydroponic lettuce with deficiency")
   #set an image
   st.image("https://whyfarmit.com/wp-content/uploads/2021/11/Green-oakleaf-lettuce-lifted-from-aquaponic-system.jpg", caption = "Hydroponics")
   #what it ldficiency
   st.subheader("What is hydroponic lettuce with deficiency?")
   st.write("In lettuce, calcium deficiency often manifests as tip burn on developing leaves. Tip burn gives leaf margins a burned or crinkled appearance and will affect their appearance throughout development. The damage continues to affect new leaves until the cause of the deficiency is remedied.")
   st.subheader("Symptoms of Hydroponic Lettuce with Deficiency?")
   st.write("You'll notice stunted leaves, chlorosis, deformed leaves, necrotic spots, and leaves with wavy outlines.")
   st.subheader("How to Avoid?")
   st.write("Nitrogen deficiency can be corrected by applying either organic or inorganic fertilisers, but nitrate or ammonium-based fertilisers work the most quickly. Any general-purpose “grow” formula will usually provide enough nitrogen to correct major deficiencies.")

#setting the tabs
tab1, tab2  = st.tabs(["About ❓", "Predictions 📈"])

with tab1:
   st.header("About the Project 🔖")
   st.markdown("This web app helps you to identify hydroponic lettuces with deficiency.")
   html_code = """
   <p>To get predictions, select the prediction tab and upload an image. Then the app will classify the image to 4 categories as,</p>
   <ul>
    <li>Fully Nutritional</li>
    <li>Potassium Deficient</li>
    <li>Phosphorus Deficient</li>
    <li>Nitrogen Deficient</li>
   </ul>
   """
   st.markdown(html_code, unsafe_allow_html=True)

   #displaying sample images
   st.subheader("Sample Images for Each Category 🥦")

   grid_image = """
      <div class="grid-container">
         <div class="grid-item">
               <img class = "img" src = "https://storage.googleapis.com/kagglesdsdata/datasets/2859704/4931391/FNNPK/FN/fn3.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230426%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230426T043538Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=918f61bf4160b68732a7bd4815ee1679c556c504d7af5d6040807ce4b74c8de115ef9e296b6dcb8e2dc33e5049fb9a480d6f7e8daedf793f241e8d2236bc69db048061aa4f86f3bf605f86ebd798fc1439f1db50b499a33f07b44a7d3dc7c1fc6b3fbdee4f1cb43a21473e4ae3e19dee107032b7a84ffba0efa09ad4b4953730917c3c6bb7b8b11332061ec6b53d2d54b7a594071c32c404baed59e27310e190b45229b3b4e2d526fc4975965b052de880b13a507904f6ca889fc00d41ab27fd9adfc63b2caa13e98649433a6ee6283d050752a82c86923455d9babf2e19769c7220cc5dc7b2f1642acdd9f0ebd2b05a7b652e9aab750213e6ec13a79d005c00" alt = "fully-nutritional">
               <p class = "label">Fully Nutritional</p>
         </div>
         <div class="grid-item">
               <img class = "img" src = "https://storage.googleapis.com/kagglesdsdata/datasets/2859704/4931391/FNNPK/-K/k_13.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230426%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230426T043314Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=59dabc3cc3fd1d195d89823b0ec1715522bfccab70d4be55e8b9fd598b71b3da33483e4e3b5f1e11dd8faf89b872b03b5ee7dd8f49077916482818cce3f9b101ee3ea5dccd0c7df050f3a55c4fdcb727c339d6597158687aa8116def72d78386eebf9ecb1bde92a0e981d2c4bc03041e7670219c1c116326e880c2192923553b29d0498714519695f29067c7db37e7ebc0c54626433b8d1fed15b5741492fc658b8d9d26aa7b439e0ebf054520504b7e400c569162235907ed7fdf4e1ad0bb934af6811ab0db93dcd219071eb501b5013e946035c14308537ac8cc53b639371577b9bd3ba3b41ad1ca79de1ea42a7f4b90afe8a83fe22d727d0969124b84c205" alt = "Potassium Deficient">
               <p class = "label">Potassium Deficient</p>
         </div>
         <div class="grid-item">
               <img class = "img" src = "https://storage.googleapis.com/kagglesdsdata/datasets/2859704/4931391/FNNPK/-P/p2.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230426%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230426T043410Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=59cda20447b6c5476320af18c525712133885d3a3f5837cffd968cfa95dee18e51b16572e997de9f0127fab4aca8c3d0d435712aa63a36a798088af1d89eff7849aff4c17a13af8548c694921fcc9fb0abc97f822669c0cba31246e81e2fd8f67f67ec738076631a3567a962568ffa2df704686c0816ba5b6256686eeb5f2454f20d4d4a65b3628cecdc9fd7e0671ef31d900d5477ea967b7e631481a0792906874815abee6e62bcdb6cd87f83b46ef003676b825d6b47123b618c0b8e6a95aac94c94601422fc5dac382691e9cfaf8cd50e6f203b8b3b0cbf3a8eb58c906da7559eecc6d3a33a861a5ed34b39938032ee963452fe8c1d9505e8b01c866795f2" alt = "phosphorus Deficient">
               <p class = "label">Phosphorus Deficient</p>
         </div>  
         <div class="grid-item">
               <img class = "img" src = "https://storage.googleapis.com/kagglesdsdata/datasets/2859704/4931391/FNNPK/-N/n_1.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230426%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230426T043006Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=3f4d8df0d19c52a8c4b38a5c98edd43544cab56fa66bf2dfcb13d8aefd194103d77177052f458168bbbd2f09fcbb9db436002297784a8401a9567fd82632f53bab2960d050de8ae91b8a564b543a98f7a8989014fe88766bc84e0508d4831e68c250cf25020446a440fdeaf2c52298b5fb77089b22b990a76859d0a8280d4dd30a9b2a3b402e2acf1a6a7e7a779f529b7509cca0daccddd5e103256b98cd32d9239818b9314c1c1f62e372d446a1d3135588cb2649530fc7390355031e73834505999416bb517702fef253aa855026c0c8d432ba028d0b8efd4108475136e6a12c731c46a55f830f7a61dcf364c2187d3209d3b3ac01182a165de7348a231948" alt = "Nitrogen Deficient">
               <p class = "label">Nitrogen Deficient</p>
         </div>
      </div>
    """
   st.markdown(grid_image, unsafe_allow_html=True)

with tab2:
   st.header("Prediction Dashboard 🖥️")
   #dropdown to select the prediction method
   st.subheader("Select a Prediction Method ⬇️")
   option = st.selectbox("How would you like to make the predictions?",("Image URL","Image Upload"))

   if option == "Image URL":
      st.subheader("Predictions using Image URL 🔗")
      #helper image links to predict the images
      helper_links = """
         <div class = "about">
            <h4>Use these test image links to predict and get the results..</h4>
            <ul>
               <li>Fully-Nutritional - <a class = "link" href = "https://gardenerspath.com/wp-content/uploads/2021/07/How-to-Grow-Buttercrunch-Lettuce-Cover.jpg">Image Link</a></li>
               <li>Potassium Deficient - <a class = "link" href = "https://www.haifa-group.com/files/Deficiencies/Vegetables/Lettuce/lettuce_macro_Mg-magnesium.jpg">Image Link</a></li>
               <li>Phosphorus Deficient - <a class = "link" href = "https://static.wixstatic.com/media/c43ec8_79335d71a8e841b8ac1653e97fb23583~mv2.jpg/v1/fill/w_498,h_498,al_c,q_85,usm_0.66_1.00_0.01/c43ec8_79335d71a8e841b8ac1653e97fb23583~mv2.jpg">Image Link</a></li>
               <li>Nitrogen Deficient - <a class = "link" href = "https://i0.wp.com/www.nosoilsolutions.com/wp-content/uploads/2019/10/vegetativestage.jpg?fit=800%2C534&ssl=1">Image Link</a></li>
            </ul>
         
         </div>
      """
      st.markdown(helper_links, unsafe_allow_html=True)
      image_link = st.text_input("Input Image URL")
      
      if image_link:
         st.image(image_link, caption = "Input Image")

         #setting the headers and data
         headers = {
            'Prediction-Key': subscription_key,
            'Content-Type': 'application/json'
         }

         data = {
            'url': image_link
         }
         response = get_prediction_link(data, headers)
         st.subheader("This is {}".format(response['predictions'][0]['tagName']))

   if option == "Image Upload":
      st.subheader("Predictions by Uploading an Image 🖼️")
       #predictions by uploading an image
      image_file = st.file_uploader("Please upload an image", accept_multiple_files=False, help="Add a supportive image type")

      if image_file:
         image = Image.open(image_file)
         image.save('input.png')

         st.image(image)

         with open('input.png', 'rb') as img:
               image_content = img.read()

               headers = {
                  'Prediction-Key': subscription_key,
                  'Content-Type': 'application/octet-stream'
               }
               response = get_prediction_image(image_content, headers)
               st.subheader("This is {}".format(response['predictions'][0]['tagName']))
