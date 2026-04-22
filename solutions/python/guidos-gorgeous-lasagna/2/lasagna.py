EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the baking time remaining.

    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - amount of time remaining for the lasagna to finish baking.

    This function takes an integer the
    time already spent baking and calculates how much time remains before the lasagna
    finishes baking.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes (number_of_layers):
    """Calculate the lasagna preparation time

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time spent preparing the lasagna

    This function takes an integer representing the number of lasagna layers and calculates the time
    spent layering the lasagna
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time