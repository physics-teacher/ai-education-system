from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='en')
def extract_text(image_path):
	result = ocr.ocr(image_path)
	text = "" 
	for line in result:
		text += line[1][0] + "\n"
		return text

if __name__ == "__main__":
	image = "../datasets/sample_image.jpg"
	text = extract_text(image)
	print("Extracted Text:\n")
	print(text)
		





