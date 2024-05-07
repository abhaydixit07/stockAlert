class ProjectMetricsEstimator:
    def __init__(self):
        pass
    
    def calculate_function_points(self):
        # Define complexity weights for inputs, outputs, inquiries, files, and interfaces
        complexity_weights = {
            'inputs': 4,
            'outputs': 5,
            'inquiries': 4,
            'files': 10,
            'interfaces': 7
        }
        
        # Calculate Total Degree of Influence (TDI)
        tdi = sum(complexity_weights.values())
        
        # Determine General System Characteristic (GSC) based on TDI
        # For simplicity, let's assume GSC is 1 for this example
        gsc = 1
        
        # Calculate Function Points (FP)
        fp = gsc * tdi
        return fp
    
    def calculate_basic_cocomo(self, size):
        # Mode of the project (organic, semi-detached, embedded)
        mode = 'organic'  # Assume organic mode for this example
        
        # Effort multipliers and scale factors (for organic mode)
        a, b, c, d = 2.4, 1.05, 2.5, 0.38
        
        # Calculate Effort
        effort = a * (size ** b)
        
        # Calculate Duration
        duration = c * (effort ** d)
        
        return effort, duration
    
    def calculate_intermediate_cocomo(self, size):
        # Define project characteristics ratings
        ratings = {
            'product': 'high',
            'hardware': 'low',
            'personnel': 'high',
            'project': 'high'
        }
        
        # Effort multipliers for each characteristic
        effort_multipliers = {
            'low': 0.9,
            'nominal': 1,
            'high': 1.1
        }
        
        # Adjust size based on ratings
        adjusted_size = size * (effort_multipliers[ratings['product']] 
                                * effort_multipliers[ratings['hardware']]
                                * effort_multipliers[ratings['personnel']]
                                * effort_multipliers[ratings['project']])
        
        # Adjust nominal schedule
        nominal_schedule = 3  # Assume nominal schedule in terms of calendar months
        
        # Adjust based on risk factors (not implemented for simplicity)
        adjusted_schedule = nominal_schedule
        
        return adjusted_size, adjusted_schedule


# Project Report Metrics Estimation
if __name__ == "__main__":
    estimator = ProjectMetricsEstimator()
    
    # Function Points Estimation
    function_points = estimator.calculate_function_points()
    print("Function Points:", function_points)
    
    # Basic COCOMO Model Estimation
    size = function_points  # For simplicity, using function points as size
    basic_effort, basic_duration = estimator.calculate_basic_cocomo(size)
    print("Basic COCOMO Model:")
    print("Effort:", basic_effort, "person-months")
    print("Duration:", basic_duration, "months")
    
    # Intermediate COCOMO Model Estimation
    intermediate_size, intermediate_schedule = estimator.calculate_intermediate_cocomo(size)
    print("Intermediate COCOMO Model:")
    print("Adjusted Size:", intermediate_size)
    print("Adjusted Schedule:", intermediate_schedule, "months")
