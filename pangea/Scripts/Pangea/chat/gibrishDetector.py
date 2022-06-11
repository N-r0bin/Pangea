from gibberish_detector import detector
Detector = detector.create_from_model('big.model')
print(Detector.is_gibberish('ertrjiloifdfyyoiu'))