import click
import logging # logging module for error logging and tracking 

def setup_logging():
	logging.basicConfig(level=logging.INFO, # set logging level to INFO to capture all info/warnings/error msg
    format='%(asctime)s - %(levelname)s - %(message)s') #define format for log messages - timestamp: log level: & the message itself 

def handle_error(func):
	def wrapper(*args, **kwargs):
		try: 
		return func(*args, **kwargs)
	except Exception as e: 
		click.echo(f"this is bad: {str(e)}", err=True)
		logging.error(f"Error in {func.__name__}: {str(e)}")
	return wrapper
