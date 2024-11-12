from conda_recipe_manager.unit.recipe_manager import (
    create_recipe,
    get_recipe,
    update_recipe,
    delete_recipe
)


def test_recipe_lifecycle():
    # Create a new recipe
    recipe_name = "integ_test_recipe"
    dependencies = ["numpy", "pandas"]
    created_recipe = create_recipe(recipe_name, dependencies)
    assert created_recipe["status"] == "created"

    # Retrieve the recipe and check details
    retrieved_recipe = get_recipe(recipe_name)
    assert retrieved_recipe["name"] == recipe_name
    assert retrieved_recipe["dependencies"] == dependencies

    # Update the recipe
    new_dependencies = ["elasticsearch", "logstash"]
    updated_recipe = update_recipe(recipe_name, new_dependencies)
    assert updated_recipe["status"] == "updated"
    assert updated_recipe["dependencies"] == new_dependencies

    # Delete the recipe
    delete_status = delete_recipe(recipe_name)
    assert delete_status == "deleted"

    # Verify the recipe no longer exists
    with pytest.raises(KeyError):
        get_recipe(recipe_name)
