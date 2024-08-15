from PIL import Image as PILImage
import google.generativeai as genai
from io import BytesIO

genai.configure(api_key="AIzaSyDeEkaXQii54G7obTPFuqUyd3yVReBdUM4")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 0.2,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="""
    
  You will be working to complete a functionality. 
  You will be provided with images [ that to be clicked through phones ] which will contain objects that can be recycled and can't be recycled

  You have to categorize the objects in the images and return JSON code of the same (seggregate objects having common categories) 
  Also Include what objects are under sub-category and item in sub-category should not be repetable.
  The sub-category can be only Plastic, Metal, Electornics, Wood etc and items can be what are the specific respective to them.
  And don't count objects , just fit the occurance in categories and seggregate common occurances. 
  Again don't dive into the classification , your task is to just provide basic-intermediate classification.

  Main Categories : 
    1. Recyclable / Reusable objects
    2. Non-Recyclable Objects

    
Just an over-exerted example for basic understanding , don't copy from this: 
{
    "Recyclable / Reusable Objects": 
    {
        "Sub-Category 1": ['item 1' , 'item 2' ],
        "Sub-Category 2" : ['item 1' , 'item 2']
    }

    "Non Recyclable Objects ":{
        "Sub-Category  3" : [ 'item 1' ]
    }

}

    Research on the objects in the image weather they are recyclable or non-recyclable not based on your data ,
    based on latest google search feed for particular object you interpreted from image.
    
    Notes:  

    1. Image may be focusing on single or multiple items at the same time. Take time to consider what to include in your response.

    2. Your maximum image capacity will be 5 images at a time. Generate a single JSON code for all images if multiple images are provided.
     
    3. For every item in image it could not focus on image what is meant to be focused on. The user will upload the image with intention of showing object
     that he needs you to detect and categorize. Do not consider every item or item that seems to be incomplete in the image. 
     Try to add items that take more space in image and exclude those items in background.
    4. Try to fit the object in only one category , don't just do the blind accuracy work with analization of images.
    
    EXTRA IMPORTANT INSTRUCTIONS :
    1. re-check the JSON for possible mistakes , again we need to deliver the result with highest precision you can provide.

    2. Try to not mix the same items in different categories. Again do the research and Try to reduce the errors in JSON because, 
    the functionaliy to work the JSON needs to be accurate.


    """,
)


def generate_json_from_images(image_list):
    chat_session = model.start_chat(history=[])
    image_to_detect=[]
    for image in image_list:
        image_data=image.read()
        pil_image=PILImage.open(BytesIO(image_data))
        image_to_detect.append(pil_image)

    response = chat_session.send_message(image_to_detect)
    return response.text