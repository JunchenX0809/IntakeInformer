# intakeinformer

A nutritional tracker warpped around the USDA FoodData Central API. The warpper allows users to track their daily food intake and analyze the nutritional content of their diet based on the USDA food database and their own selections.

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
   
### Step 3: Install and Use IntakeInformer
1. **Install the Package:**
   - Use pip (or poetry if you're using it) to install `IntakeInformer`.
   - Command: `pip install IntakeInformer` (or the appropriate command if using poetry).

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


## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`intakeinformer` was created by Junchen Xiong. It is licensed under the terms of the MIT license.

## Credits

`intakeinformer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
