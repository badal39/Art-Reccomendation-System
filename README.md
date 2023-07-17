# Baroque-inspired Art Recommendation System

The Baroque-inspired Art Recommendation System is an advanced recommendation system developed using Python and Streamlit. It combines the power of BERT for text feature extraction and utilizes ResNet-50 for image feature extraction. By merging these features, the system creates a unique representation for personalized art recommendations, enabling a holistic approach to personalized art suggestions.

## Features
- Text feature extraction using Transformers and BERT.
- Image feature extraction using ResNet-50.
- Merging of text and image features to create personalized art recommendations.
- Streamlit integration for a user-friendly interface.

## Approach
The Baroque-inspired Art Recommendation System follows a multi-step approach  consists of the following stages:

1. Data Collection:
- The system collects art data from the WikiArt dataset, which is a large repository of artworks from various artists and genres, including Baroque-inspired art.

2. Preprocessing:
- The textual descriptions of the art pieces are preprocessed by removing unnecessary characters, converting to lowercase, and tokenization. This step helps in standardizing and cleaning the text data.
- Image preprocessing consists of a series of transformations to preprocess the input image, including resizing, cropping, converting to a tensor, and normalizing the pixel values.

3. Feature Engineering:
- Text Feature Extraction: The system utilizes BERT to extract meaningful features from the preprocessed textual descriptions of the art pieces. These models capture the semantic meaning and context of the text, enabling the system to understand the characteristics of the artwork.
- Image Feature Extraction: The system employs ResNet-50 to extract high-level features from the preprocessed art images. Bypassing the images through ResNet-50, the system captures visual information such as colors, shapes, and textures.
- The extracted text and image features are then combined or fused to create a unified representation of the art pieces. This fusion allows the system to capture both the textual and visual aspects of the artwork in a comprehensive manner.

4. Recommendation Generation:
- Cosine Similarity: The system utilizes cosine similarity as a measure of similarity between the feature representations of art pieces. Cosine similarity calculates the cosine of the angle between two vectors, providing a similarity score between 0 and 1.
- To generate recommendations, the system compares the feature representation of a given art piece with the feature representations of other art pieces in the dataset. The system identifies the most similar art pieces based on their cosine similarity scores.
- The top-n most similar art pieces are recommended to the user, providing personalized suggestions that align with their preferences and interests.



## Result
The Baroque-inspired Art Recommendation System showcases the power of combining text and image features for personalized art recommendations. By utilizing  BERT, and ResNet-50, the system offers users a holistic approach to discovering and enjoying Baroque-inspired art pieces.

## Installation
To run the Baroque-inspired Art Recommendation System, follow these steps:

1. Clone the repository:

   git clone https://github.com/badal39/Art-Reccomendation-System.git

3. Create a virtual environment:

   python -m venv env

5. Activate the virtual environment:

# For Windows
env\Scripts\activate

# For Linux/Mac
source env/bin/activate

4. Install the required dependencies:

    pip install -r requirements.txt

   
## Usage
1. Run the Streamlit app: streamlit run App.py
3. Open your web browser and go to `http://localhost:8501` to access the application.
4. Follow the instructions on the web interface to use the Baroque-inspired Art Recommendation System.



