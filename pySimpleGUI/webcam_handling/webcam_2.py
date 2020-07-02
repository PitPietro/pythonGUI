import PySimpleGUI as simpleGUI
import cv2


'''
https://www.reddit.com/r/Python/comments/cpymni/7_lines_of_python_code_to_show_your_webcam_in_a/


'''


def cam_2():
    window = simpleGUI.Window(
        'Demo Application - OpenCV Integration',
        [
            [simpleGUI.Image(filename='', key='image')],
        ],
        location=(800, 400)).Finalize()
    window.Maximize()

    cap = cv2.VideoCapture(0)  # Setup the camera as a capture device

    while True:  # The PSG "Event Loop"
        event, values = window.Read(timeout=20, timeout_key='timeout')  # get events for the window with 20ms max wait
        if event is None:
            break  # if user closed window, quit
        window.FindElement('image').Update(
            data=cv2.imencode(
                '.png',
                cap.read()[1])[1].tobytes()
        )  # Update image in window


def cam_2_v2():
    # define the window layout
    layout = [[simpleGUI.Image(filename='', key='_IMAGE_')]]

    # create the window and show it without the plot
    window = simpleGUI.Window('Demo App - OpenCV Integration', layout,location=(800, 400))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)  # Setup the OpenCV capture device (webcam)
    while True:
        event, values = window.Read(timeout=20, timeout_key='timeout')
        if event is None:
            break
        ret, frame = cap.read()  # Read image from capture device (camera)
        img_bytes = cv2.imencode('.png', frame)[1].tobytes()  # Convert the image to PNG Bytes
        window.FindElement('_IMAGE_').Update(data=img_bytes)  # Change the Image Element to show the new image


if __name__ == '__main__':
    cam_2_v2()
