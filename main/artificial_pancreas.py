class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise
    MINIMUM_GLUCOSE = 70         # minimum safe glucose level


    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self.insulin_administered = 0
        

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        if carbs < 0:
            raise ValueError("Food Carbs cannot be negative.")
        self.glucose_level += carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB
        

    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        if duration < 0:
            raise ValueError("Duration of exercise cannot be negative.")
        self.glucose_level -= duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN 
        print(f"exercise {self.glucose_level}, {duration}")
        if self.glucose_level < ArtificialPancreasSystem.MINIMUM_GLUCOSE:
            self.glucose_level = ArtificialPancreasSystem.MINIMUM_GLUCOSE
        

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        print(f" action {self.glucose_level}")
        if (self.target_glucose - self.tolerance ) <=self.glucose_level <= (self.target_glucose + self.tolerance):
            return "maintain", ""
        
        elif self.glucose_level > (self.target_glucose + self.tolerance):
            insulin_needed =  (self.glucose_level - self.target_glucose) * self.insulin_sensitivity 
            self.insulin_administered += insulin_needed
            return "administer_insulin", insulin_needed

        elif self.glucose_level < self.target_glucose - self.tolerance:
            return "warn_low_glucose", ""
    
    def administer_insulin(self, units: float):
        """Administer insulin to lower glucose levels."""
        self.glucose_level -= units * self.insulin_sensitivity
        self.insulin_administered += units
        if self.glucose_level < ArtificialPancreasSystem.MINIMUM_GLUCOSE:
            self.glucose_level = ArtificialPancreasSystem.MINIMUM_GLUCOSE
        
        
         
            




# controller = ArtificialPancreasSystem(100, 1.0, 100, 10)
# action, level = controller.predict_action()
# print(action, level)
# controller.meal(40)
# controller.exercise(20)
# action, level = controller.predict_action()
# print(action, level)
# controller.exercise(250)
# action2, level2 = controller.predict_action()
# print(action2, level2)
