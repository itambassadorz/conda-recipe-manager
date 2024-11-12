import pytest
from conda_recipe_manager.unit.recipe_manager import create_recipe


def test_create_recipe_success():
    recipe_name = "test_recipe"
    dependencies = ["numpy", "pandas"]
    result = create_recipe(recipe_name, dependencies) # Call the function
    # Assert the expected output
    assert result["name"] == recipe_name
    assert result["dependencies"] == dependencies
    assert result["status"] == "created"


def test_create_recipe_missing_name():
    dependencies = ["numpy", "pandas"]
    # Expect a ValueError if name is missing
    with pytest.raises(ValueError):
        create_recipe("", dependencies)
