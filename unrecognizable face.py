import vlc
import cv2
import numpy as np
import time

class myclass():
	def __init__(self):
		self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		self.detector_eyes = cv2.CascadeClassifier("haarcascade_eye.xml")
		self.cap = cv2.VideoCapture(0)


	def detect_face_and_eyes(self):
		Checkered = input("If you want your face to be displayed unrecognizable please enter 1, otherwise enter 0: ")

		while True:
			ret, frame = self.cap.read()

			if ret:
				frame = cv2.flip(frame, 1)
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				results = self.detector.detectMultiScale(gray)
				for (x, y, w, h) in results:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
					
					gray_eyes = gray[y:y+h , x:x+w]
					# print(x , y, w, h)
					# print(gray_eyes.shape)

					results_eyes = self.detector_eyes.detectMultiScale(gray_eyes)

					if Checkered == '1':
						kernel_size = 9
						blur = cv2.GaussianBlur(frame[y:y+h , x:x+w], (kernel_size, kernel_size), 0)
						for i in range(0,15):
							blur = cv2.GaussianBlur(blur, (kernel_size, kernel_size), 0)

						blur_show = frame.copy()
						blur_show[y:y+h , x:x+w] = blur

						for (xs, ys, ws, hs) in results_eyes:
							cv2.rectangle(blur_show, (xs+x, ys+y), (xs+x+ws, ys+y+hs), (0, 255, 0), 2)

						cv2.imshow("Webcam", blur_show)

					else:

						for (xs, ys, ws, hs) in results_eyes:
							cv2.rectangle(frame, (xs+x, ys+y), (xs+x+ws, ys+y+hs), (0, 255, 0), 2)

						cv2.imshow("Webcam", frame)

				q = cv2.waitKey(1)
				if q == ord('q'):
					break
			else:
				break

		self.cap.release()
		cv2.destroyAllWindows()


	def choose_an_art_product(self):
		product = input("Hello! If you want a music please enter 'music'\n"
               "If you want a movie please enter 'movie'\n"
               "And if you want a book please enter 'book'\n")

		if product == 'music':
			
			music = vlc.MediaPlayer('Farhad Najva.mp3')
			music.play()
			time.sleep(191)


		elif product == 'movie':
	
			cap = cv2.VideoCapture('1434659607842-pgv4ql-1616202487121.mp4')
			while True:
				ret, frame = cap.read()
				if ret:
					frame = cv2.flip(frame, 1)
					cv2.imshow("Webcam", frame)
					q = cv2.waitKey(25)
					if q == ord('q'):
						break
				else:
					break

			cap.release()
			cv2.destroyAllWindows()	


		elif product == 'book':
			print('Dead Poets Society')

		else:
			print('Please enter the correct category:)')


mc = myclass()
mc.detect_face_and_eyes()
# mc.choose_an_art_product()