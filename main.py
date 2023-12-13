import cv2 as cv

video = cv.VideoCapture('movie.mp4')
fps = video.get(cv.CAP_PROP_FPS)

print('frames per second =',fps)

minutes = 0
seconds = 0
frame_id = int(fps*(minutes*60 + seconds))
print('frame id =',frame_id)

path = 'Frames'

try:
  frame_id = 0
  while(True):
    video.set(cv.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    frame_path = f'{path}/frame{frame_id}.png'

    frame_id = frame_id + 50
    cv.imwrite(frame_path, frame)
except:
  pass