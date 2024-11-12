from conda_recipe_manager.unit.recipe_manager import update_recipe


def test_update_recipe():
    recipe_name = "test_recipe"
    new_dependencies = ["elasticsearch", "logstash"]
    updated_recipe = update_recipe(recipe_name, new_dependencies) # update_recipe returns the updated recipe data
    assert updated_recipe["name"] == recipe_name
    assert updated_recipe["dependencies"] == new_dependencies
    assert updated_recipe["status"] == "updated"


def test_update_nonexistent_recipe():
    # Test updating a recipe that doesn't exist
    with pytest.raises(KeyError):
        update_recipe("nonexistent_recipe", ["numpy"])
