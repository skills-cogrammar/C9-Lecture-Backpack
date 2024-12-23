# Import logging (Logging library to be used that comes with python)
import logging

# Configure logging
logging.basicConfig(
    filename='app.log', # Creates a log file called app.log
    filemode='w', # Write into the created log file
    format='%(asctime)s - %(levelname)s - %(message)s', #2024-12-23 - DEBUG - Process number 1 starting
    level=logging.DEBUG # Start from the DEBUG level
)

'''
Create a function that takes in a list of 
integers and outputs the square of the integers
'''
def process_numbers(numbers):
    logging.info('Starting the process_number function.')
    results = []

    for i, number in enumerate(numbers):
        try:
            logging.debug(f"Processing index {i}: number={number}")
            if not isinstance(number, (int, float)):
                raise ValueError(f"Invalid number at index {i}: number={number}")
            square = number ** 2
            results.append(square)
            logging.info(f"Successfully processed index {i}: square={square}")
        except Exception as e:
            logging.error(f"Error in processing index {i}: {e}")

    logging.info("Finished processing numbers")
    return results



if __name__ == "__main__":
    numbers = [10, 20, "30", 100, -10]
    logging.info("Application has started")
    outcome = process_numbers(numbers)
    logging.info(f"Final results: {outcome}")
    logging.info("Application has finished.")

