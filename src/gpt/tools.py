## load recipe data from a JSON file
import json

recipe_path = "database/mock_data.json"
recipe_data = json.load(open(recipe_path))

def get_recipe_data(recipe_name: str) -> dict:
    """Fetches recipe data for a given recipe name"""
    return recipe_data.get(recipe_name, {})

tools = [
    {"type": "function",
     "function": {
         "name": "get_recipe_data",
         "description": "Fetches recipe data for a given recipe name",
         "parameters": {
             "type": "object",
             "properties": {
                 "recipe_name": {
                     "type": "string",
                     "description": "The name of the recipe to fetch data for"
                    }
                },
             "required": ["recipe_name"],
             "additionalProperties": False
            }
        }
    }
]