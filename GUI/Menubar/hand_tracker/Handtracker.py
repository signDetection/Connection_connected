import cv2
import mediapipe as mp


class HandDetection:

    def __init__(self, video_source=0):

        self.cap = cv2.VideoCapture(video_source)

        # Get video source width and height
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if not self.cap.isOpened():
            raise ValueError("Unable to open video source", video_source)

        mphands = mp.solutions.hands
        hands = mphands.Hands()
        mpdraw = mp.solutions.drawing_utils

        while True:
            success, img = self.cap.read()
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for handNo in results.multi_hand_landmarks:
                    mpdraw.draw_landmarks(img, handNo, mphands.HAND_CONNECTIONS)

            cv2.imshow('LIVE', img)
            key = cv2.waitKey(20)

            if key & 0XFF == ord('q'):
                break

            if key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

    # def get_frame(self):
    #     if self.cap.isOpened():
    #         ret, frame = self.cap.read()
    #         if ret:
    #             # Return a boolean success flag and the current frame converted to BGR
    #             return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         else:
    #             return ret, None
    #
    # def __del__(self):
    #     if self.cap.isOpened():
    #         self.cap.release()


def hand_moment_detector():
    HandDetection()


if __name__ == "__main__":
    hand_moment_detector()
