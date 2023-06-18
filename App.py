import streamlit as st
import json
from PIL import Image
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# Watch This Video for image grid
# https://www.youtube.com/watch?v=GG6WDeLmw6w

def Reccomend_art(merged_final_features,user_selected_indices):
    # Merged User Selected Inndexs of that featues
    user_selected_features = merged_final_features[user_selected_indices]
    ## Calculate Similarities between User Selected index and other images
    similarity_scores = cosine_similarity(user_selected_features, merged_final_features)
    
    #Sort and Retrieve Top Similar Images
    similar_images_indices = similarity_scores.argsort(axis=1)[:, ::-1]  # Sort indices in descending order
    recommended_images_indices = similar_images_indices[:, 1:6]  # Retrieve top 5 similar images (excluding the selected images)

    # recommended  and 6 random images from most similar images 5 from each index
    rec_index = np.random.choice(recommended_images_indices.flatten(), size=6, replace=False)

    return rec_index

def display_images(images,artist_name,image_name):
                            num_images = len(images)
                            num_rows = (num_images + 2) // 3  # Calculate the number of rows needed

                            for row in range(num_rows):
                                col1, col2, col3 = st.columns(3)  # Split the row into three columns

                                # Display the images in each column
                                if row * 3 < num_images:
                                    col1.image(images[row * 3], use_column_width=True)
                                    col1.caption(image_name[row * 3].capitalize())
                                    col1.markdown('Artist : **'+artist_name[row * 3].capitalize()+'**.')

                                if row * 3 + 1 < num_images:
                                    col2.image(images[row * 3 + 1], use_column_width=True)
                                    col2.caption(image_name[row * 3 + 1].capitalize())
                                    col2.markdown('Artist : **'+artist_name[row * 3 + 1].capitalize()+'**.')

                                if row * 3 + 2 < num_images:
                                    col3.image(images[row * 3 + 2], use_column_width=True)
                                    col3.caption(image_name[row * 3 + 2].capitalize())
                                    col3.markdown('Artist : **'+artist_name[row * 3 + 2].capitalize()+'**.')
        ## Load Featuress Array



@st.cache_data 
def load_features_array():
    merged_final_features = np.load('./DATA/final_features.npy')

    return merged_final_features




@st.cache_data 
def load_image_catalog():
    with open('./DATA/image_catalog.json', 'r') as file:
            image_catalog  = json.load(file)
    return image_catalog

@st.cache_data
def load_image_options(image_catalog):
    image_options =  [row[2] for row in image_catalog.values()]

    random.shuffle(image_options)
    return image_options

@st.cache_data 
def load_image_des_key():
    with open('./DATA/des_key.json', 'r') as file:
            des_key  = json.load(file)
    return des_key

# st.write('hello')

## Load Image Catalog
image_catalog = load_image_catalog() 

## Load Keys For Description
des_key = load_image_des_key()

# Selecteing image_options name as description of image
image_options =  load_image_options(image_catalog)
# random.shuffle(image_options)

st.title("Baroque Artwork Recommendation")
st.caption("Step into the opulent world of Baroque art with our Art Recommendation Project. Immerse yourself in the extravagant beauty and grandeur of this artistic movement, characterized by its ornate detailing, dramatic compositions, and lavish aesthetics. With our carefully curated collection of Baroque artworks, we invite you on a journey through time, exploring the works of renowned Baroque masters and discovering hidden gems of this captivating period")


tab1, tab2 = st.tabs(["Selecte Image's", "Reccomend"])
                    


with tab1:
            # Display thumbnail images corresponding to the selected image options
            selected_images = st.multiselect("Select Images", image_options, default=None, key="selected_images")
            user_selected_indices = []
            if len(selected_images) > 0:
                    

                    processed_images = []
                    artist_name_lst = []
                    image_name_lst = []
                    for image_name in selected_images:
                        key = des_key[image_name]
                        user_selected_indices.append(key)
                        image_path = image_catalog.get(str(key))[0]
                        artist_name = image_catalog.get(str(key))[1]

                        img = Image.open(image_path)
                        ## append Process Image
                        processed_images.append(img)
                        ## Append Artist name
                        artist_name_lst.append(artist_name)
                        ## Append Image Caption
                        image_name_lst.append(image_name)
            ## Function For Displaying Image in row
            
                    display_images(processed_images,artist_name_lst,image_name_lst)
            

            else:
                    st.subheader("Select your preferences ART from the Dropdown, and we'll recommend some magnificent Baroque masterpieces.")








with tab2:
    if len(user_selected_indices) > 1 :
            

                merged_final_features = load_features_array()
                recc_index = Reccomend_art(merged_final_features,user_selected_indices)
                processed_images = []
                artist_name_lst = []
                image_name_lst = []

                for i in range(len(recc_index)):
                    image_path = image_catalog.get(str(recc_index[i]))[0]
                    artist_name = image_catalog.get(str(recc_index[i]))[1]
                    image_name = image_catalog.get(str(recc_index[i]))[2]
                    img = Image.open(image_path)
                    ## append Process Image
                    processed_images.append(img)
                    ## Append Artist name
                    artist_name_lst.append(artist_name)
                    ## Append Image Caption
                    image_name_lst.append(image_name)

                ## Function For Displaying Image in row
                display_images(processed_images,artist_name_lst,image_name_lst)

    else: 
           st.write('Selecte not just one, but multiple images for an exquisite art recommendation ')

