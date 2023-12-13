import requests
import os
import json
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
import pandas as pd

FDC_key = os.getenv('POETRY_FDC_API_KEY')

def catbind(a, b):
    concatenated = pd.concat([pd.Series(a.astype("str")),
                              pd.Series(b.astype("str"))])
    return pd.Categorical(concatenated)
'''
internal helper function to fetch data from API and parse it into dataframe for future operation
'''

def _fetch_food_data(query):
    """
    Fetches food data from the USDA FoodData Central API using an internal API key.
    :param query: Food query.
    :return: DataFrame with food data.
    """
    url_search = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params_search = {
        "api_key": FDC_key,
        "pageSize": 10,     # number of results to return, default to 1 for ease of access
        "pageNumber": 2,   # Page number to retrieve, default to 1
        "dataType": [ "Branded"],
        "sortBy": "publishedDate",
        "sortOrder": "asc",
        "query": query
    }
    try:
    # Send a GET request
        response_food_search = requests.get(url_search, params=params_search)

    # If the response was successful, no Exception will be raised
        response_food_search.raise_for_status()
    except response_food_search.exceptions.HTTPError as http_err:
    # Specific HTTP error handling
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
    # General error handling
        print(f'Other error occurred: {err}')
    else:
    # Success
        data = response_food_search.json()

    if 'foods' in data:
        '''
        pd.json_normalize is used to flatten the nested JSON structure into a DataFrame. 
        '''
        return pd.json_normalize(data, record_path=['foods'])
    else:
        return pd.DataFrame()


def get_user_food_selection(food_df):
    """
    Presents a list of foods to the user and asks them to select one.
    :param food_df: DataFrame with food items.
    :return: The selected food item as a DataFrame row.
    """
    if food_df.empty:
        print("No foods found.")
        return None

    # Display the top results to the user
    for i, row in food_df.iterrows():
        brand_owner = row.get('brandOwner', 'No brand information')
        print(f"{i + 1}: {row['description']} ({brand_owner}, {row.get('servingSize', 'N/A')}g)")

    # Ask the user to make a selection
    try:
        choice = int(input("Enter the number of your choice: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    # Return the selected food item
    if 0 <= choice < len(food_df):
        return food_df.iloc[choice]
    else:
        print("Invalid selection.")
        return None

def calculate_calories_from_selection(selected_items):
    """
    Calculates the calorie content per 100g for user-selected food items and returns a dictionary with individual and total calories.

    Parameters
    ----------
    selected_items : list
        A list of DataFrame rows, each representing a user-selected food item. Each row should contain the food nutrients data.

    Returns
    -------
    dict
        A dictionary where each key is the food item's name, and the corresponding value is its calorie content per 100g. 
        The dictionary also includes a 'total' key representing the sum of calories from all selected items.

    Examples
    --------
    # Assuming selected_banana, selected_apple, and selected_orange are DataFrame rows obtained from user selections
    >>> selected_items = [selected_banana, selected_apple, selected_orange]
    >>> calories_content = calculate_calories_from_selection(selected_items)
    >>> print(calories_content)
    {'Banana': 89.0, 'Apple': 52.0, 'Orange': 47.0, 'total': 188.0}
    """

    calories_dict = {}
    total_calories = 0

    # Nutrient IDs
    ENERGY_ID = 1008
    CARBS_ID = 1005
    FAT_ID = 1004
    PROTEIN_ID = 1003

    for item in selected_items:
        food_name = item['description']
        food_calories = 0  # Initialize calories for this food item

        # Extract the nutrients data
        nutrients_df = pd.json_normalize(item['foodNutrients'])
        nutrients = nutrients_df.set_index('nutrientId').to_dict('index')

        # Get the serving size in grams
        serving_size = item.get('servingSize', 100)  # Default to 100g if not specified

        # Calculate calories per 100g
        if ENERGY_ID in nutrients and 'value' in nutrients[ENERGY_ID]:
            energy_per_serving = nutrients[ENERGY_ID]['value']
            food_calories = (energy_per_serving / serving_size) * 100
        else:
            # Fallback to calculating from protein, fat, and carbohydrates
            for nutrient_id, multiplier in zip([CARBS_ID, FAT_ID, PROTEIN_ID], [4, 9, 4]):
                if nutrient_id in nutrients and 'value' in nutrients[nutrient_id]:
                    nutrient_value_per_100g = (nutrients[nutrient_id]['value'] / serving_size) * 100
                    food_calories += nutrient_value_per_100g * multiplier

        # Add to the total and the dictionary
        total_calories += food_calories
        calories_dict[food_name] = food_calories

    # Add total calories to the dictionary
    calories_dict["total"] = total_calories

    return calories_dict



def plot_calorie_comparison(calorie_data):
    """
    Generates and displays a bar chart for comparing the calorie content of selected food items.

    Parameters
    ----------
    calorie_data : dict
        A dictionary where keys are food item names and values are their corresponding calorie content per 100g. 
        It should also contain a 'total' key for the sum of calories.

    Returns
    -------
    None
        This function displays a bar chart.

    Examples
    --------
    >>> calorie_data = {'BANANA FREEZE DRIED FRUIT': 2000.0, 'GALA APPLES': 28.57, 'ORGANIC VALENCIA ORANGES': 29.22, 'total': 2057.79}
    >>> plot_calorie_comparison(calorie_data)
    # This will display a bar chart comparing the calorie content of the listed food items.
    """
    if 'total' in calorie_data:
        total_calories = calorie_data.pop('total')
    
    food_items = list(calorie_data.keys())
    calories = [calorie_data[item] for item in food_items]

    plt.figure(figsize=(10, 6))
    plt.bar(food_items, calories, color='skyblue')
    plt.xlabel('Food Items')
    plt.ylabel('Calories per 100g')
    plt.title('Comparison of Calorie Content')
    plt.axhline(y=total_calories, color='r', linestyle='-', label=f'Total Calories: {total_calories:.2f}')
    plt.legend()
    plt.show()



def get_calories_for_food_query(*food_queries):
    """
    Handles fetching food data, user selection, and calculating calorie information per 100g for given food queries.

    Parameters
    ----------
    *food_queries : str
        Variable number of string arguments, each representing a food query.

    Returns
    -------
    dict
        A dictionary containing the calorie information for each selected food item per 100g, 
        as well as the total sum of calories.

    Examples
    --------
    >>> get_calories_for_food_query("banana", "apple", "orange")
    {'BANANA FREEZE DRIED FRUIT': 2000.0, 'GALA APPLES': 28.57, 'ORGANIC VALENCIA ORANGES': 29.22, 'total': 2057.79}
    """
    selected_items = []
    for query in food_queries:
        # Fetch food data
        food_df = _fetch_food_data(query)

        # Get user's selection for each query
        print(f"Select an item for '{query}':")
        selected_food = get_user_food_selection(food_df)
        if selected_food is not None:
            selected_items.append(selected_food)
        else:
            print(f"No valid selection made for '{query}'. Skipping...")

    # Calculate calories for the selected items and plot the results
    if selected_items:
        calorie_info = calculate_calories_from_selection(selected_items)
        plot_calorie_comparison(calorie_info)  # Adding visualization here
        return calorie_info
    else:
        return "No calorie information available. No valid selections were made."






