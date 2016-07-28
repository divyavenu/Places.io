from datetime import datetime

# Kudos to the following SO question for the epoch time calculations:
# http://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
epoch = datetime.utcfromtimestamp(0)

def get_epoch_time(mytime):
	return (mytime - epoch).total_seconds()

def convert_to_epoch(earliestDateStr, latestDateStr):
	# Default values to use if "None" passed in
	earliestDate = epoch
	latestDate = datetime.now()
	# Parse values from frontend
	if earliestDateStr is not None:
		earliestDate = datetime.strptime(earliestDateStr, "%m-%d-%Y")
	if latestDateStr is not None:
		latestDate = datetime.strptime(latestDateStr, "%m-%d-%Y")
	return (get_epoch_time(earliestDate),
			get_epoch_time(latestDate))

def main():
	"""
	Test cases
	"""
	print convert_to_epoch('01-02-1970', '12-31-1999')
	print convert_to_epoch(None, None)

if __name__ == "__main__":
	main()