from OCR import ocr_detect_main

import cv2
import time

def capture_image(file_name):
    cap = cv2.VideoCapture(0)  # 웹캠을 엽니다. 여러 개의 카메라가 연결된 경우 인덱스를 조정할 수 있습니다.
    
    # 웹캠 초기화 시간을 고려하여 잠시 대기합니다.
    time.sleep(2)
    
    ret, frame = cap.read()  # 웹캠에서 프레임을 읽어옵니다.
    if ret:
        cv2.imwrite(file_name, frame)  # 프레임을 이미지 파일로 저장합니다.
        # cv2.imwrite('image1/tmp.jpg',frame)
        print(f"Captured {file_name}")
    
    cap.release()  # 웹캠을 닫습니다.
    return frame

def main():
    while True:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_name = f"image/image_{timestamp}.jpg"
        frame = capture_image(file_name)
        time.sleep(5)
        ocr_detect_main(frame,file_name)
        save_path = f"result/{file_name}"
        cv2.imwrite(save_path, file_name)

if __name__ == "__main__":
    main()













