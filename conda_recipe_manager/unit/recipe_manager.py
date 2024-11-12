# Temporary in-memory database for recipes
recipes_db = {}


def create_recipe(name, dependencies):
    """
    Create a new recipe with a name and list of dependencies.
    """
    if not name:
        raise ValueError("Recipe name cannot be empty.")
    if name in recipes_db:
        raise ValueError("Recipe '{}' already exists.".format(name))
    recipe = {
        "name": name,
        "dependencies": dependencies,
        "status": "created"
    }
    recipes_db[name] = recipe
    return recipe


def get_recipe(name):
    """
    Retrieve a recipe by its name.
    """
    if name not in recipes_db:
        raise KeyError("Recipe '{}' not found.".format(name))
    return recipes_db[name]


def update_recipe(name, dependencies):
    """
    Update an existing recipe's dependencies.
    """
    if name not in recipes_db:
        raise KeyError(f"Recipe '{name}' not found.")
    recipes_db[name]["dependencies"] = dependencies
    recipes_db[name]["status"] = "updated"
    return recipes_db[name]


def delete_recipe(name):
    """
    Delete a recipe by its name.
    """
    if name not in recipes_db:
        raise KeyError(f"Recipe '{name}' not found.")
    del recipes_db[name]
    return "deleted"
