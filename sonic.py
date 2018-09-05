from ultrasonic import DistanceMeasurer


measurer = DistanceMeasurer(1, 8,7)


try: 
	measurer.setupGPIO()
	measurer.startMeasuring()
except KeyboardInterrupt:
	measurer.stopMeasuring()
