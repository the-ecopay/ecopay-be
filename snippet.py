import json


vara = '''``` json
{
    "Recyclable / Reusable objects": {
        "Metal": [
            "can",
            "tin can",
            "aluminum can"
        ]
    },
    "Non-Recyclable Objects": {
        "Plastic": [
            "plastic wrap"
        ]
    }
}```'''

cleaned_text = vara.replace('```', '')
cleaned_text=cleaned_text.replace('json','')
json_data = json.loads(cleaned_text)
print(json_data.get("Recyclable / Reusable objects"))