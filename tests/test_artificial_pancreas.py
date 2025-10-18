import pytest

import main.artificial_pancreas as ap

@pytest.mark.parametrize("meal_intake,",[(20),(4),(30)])
def test_glucose_increases_after_meal(meal_intake, system):
    start_value = system.glucose_level
    system.meal(meal_intake)
    assert system.glucose_level > start_value
    
@pytest.mark.parametrize("exercise,",[(200),(400),(500)])
def test_glucose_never_below_min(exercise,system):
    system.exercise(exercise)
    assert system.glucose_level >= ap.ArtificialPancreasSystem.MINIMUM_GLUCOSE
    

def test_glucose_decreases_after_excercise(system):
    start_value = system.glucose_level
    system.exercise(20)
    assert system.glucose_level < start_value

def test_correct_action(system):
    action,level = system.predict_action()
    assert action == "maintain"

    system.meal(50)
    action,level = system.predict_action()
    assert action == "administer_insulin"
    
    system.exercise(300)
    action,level = system.predict_action()
    assert action == "warn_low_glucose"

def test_insulin_administered_increase(system):
    start_value = system.insulin_administered
    units = 20
    system.administer_insulin(units)
    assert system.insulin_administered == start_value + units

def test_negative_value(system):
    with pytest.raises(ValueError):
        system.meal(-10)

    with pytest.raises(ValueError):
        system.exercise(-5)
    
    