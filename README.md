# intakeinformer

A nutritional tracker wrapped around [the FoodData Central USDA API](https://fdc.nal.usda.gov/api-guide.html). The wrapper allows users to track their daily food intake and analyze the nutritional content of their diet based on the USDA food database and their own selections.

#### The two core functionalities of intakeinformer – get_calories_for_food_query() and dri_benchmark() – produce distinct outputs:
- **Calorie Calculation & Comparison Visualization**: '**get_calories_for_food_query()**' calculates and returns the calorie content of a user-selected food query, normalized to a standard serving size of 100g. The calorie calculation considers the three main macronutrients (carbohydrates, fats, and proteins) of the food and generates a visualization (bar chart) depicting the calorie content per 100g of selected food items alongside a cumulative total. This visual aid helps users intuitively understand the calorie distribution of their food choices.
- **Nutrient Intake vs. DRI Recommendations**: '**dri_benchmark()**' produces a comparative bar chart that contrasts the actual nutrient intake from selected food items against [Dietary Reference Intakes (DRI)](https://www.ncbi.nlm.nih.gov/books/NBK545442/table/appJ_tab3/?report=objectonly) recommendations for a user-specified life stage. This output is instrumental in evaluating dietary choices against nutritional benchmarks.

## Installation

```python
     pip install intakeinformer
```
## Example Usage
- Because the interactive process for generating outputs with the two core functionalities of intakeinformer – **get_calories_for_food_query()** and **dri_benchmark()**. Example code & output snippets are insufficient to show the complete usage of the package's main functionalities.

Please check out an [Example Usage Showcase](docs/example.ipynb) here to see two of IntakeInformer's core functionalities in action!

## Getting Started with IntakeInformer

### Step 1: Obtain a USDA FoodData Central API Key
1. **Register for an API Key:**
   - Visit the USDA FoodData Central API's [registration page](https://fdc.nal.usda.gov/api-key-signup.html).
   - Fill in the required details and submit the form to register.
   - Once registered, you will receive an API key. Keep this key secure as it is your personal access token to the API.

### Step 2: Set the API Key as an Environment Variable
Setting the API key as an environment variable keeps it secure and easily accessible by the package.

**For Unix/Linux/macOS:**
1. Open your terminal.
2. Run the following command, replacing `'your_api_key_here'` with the actual API key you received:
   ```bash
   export POETRY_FDC_API_KEY='your_api_key_here'
3. To ensure the variable is set, you can run
   ```bash
   echo $POETRY_FDC_API_KEY
   ```
   It should display your API key.

**For Windows:**

1. **Open Command Prompt:**
   - You can search for "cmd" or "Command Prompt" in the Windows search bar and open it.

2. **Set the Environment Variable:**
   - Run the following command in Command Prompt:
     ```cmd
     set POETRY_FDC_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual API key.

3. **Verify the Environment Variable:**
   - To check if the environment variable is set correctly, run:
     ```cmd
     echo %POETRY_FDC_API_KEY%
     ```
   - This should display your API key.

### Step 3: Install and Use IntakeInformer
1. **Install the Package:**
   - Use pip (or poetry if you're using it) to install `IntakeInformer`.
   - Command: `pip install intakeinformer` (or the appropriate command if using poetry).

2. **Using IntakeInformer:**
   - Import and use the functions from IntakeInformer in your Python scripts or interactive environment.
   - Example:
     ```python
     from intakeinformer import get_calories_for_food_query, dri_benchmark

     # Use the functions as needed
     ```

### Step 4: Troubleshooting
- **API Key Issues:** If you encounter issues related to the API key (such as it not being recognized), ensure that you have correctly set the environment variable and that your current session has access to it.
- **Environment Variables:** Remember that environment variables set in a terminal session are usually temporary. If you restart your system, you might need to set the environment variable again, unless you add it to your system's permanent profile.

### Step 5: Seeking Help
- If you run into any issues or have questions, refer to the documentation of `IntakeInformer` or reach out for support as provided by the package.


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`intakeinformer` was created by Junchen Xiong. It is licensed under the terms of the MIT license.

## Credits

`intakeinformer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
