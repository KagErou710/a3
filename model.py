class testModel:
    def __init__(self):
        pass

    def predict(self, input_data):
        
        output_data = [x * 2 for x in input_data]
        return output_data
