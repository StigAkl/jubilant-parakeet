#A test-script for the DistanceMeasurer
from ultrasonic import DistanceMeasurer


measurer = DistanceMeasurer(1, 8,7)

measurer.setupGPIO()
print(measurer.getDistance())
