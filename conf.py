# regions of interest
mainROI = {'top': 650, 'left': 0, 'width': 800, 'height': 600}
frontROI = [(100, 0), (200, 0), (350, 130), (0, 130)]
laneROIHeightRange = (200, 350)
laneROIWidthRange = (250, 650)
speedROIHeightRange = (500, 530)
speedROIWidthRange = (650, 680)
speedROIWidth = speedROIWidthRange[1] - speedROIWidthRange[0]
speedROIHeight = speedROIHeightRange[1] - speedROIHeightRange[0]

# key map
FORWARD = 0
LEFT = 1
RIGHT = 2
SLOW = 3
NO_ACTION = 4

# sample parameters
FRAMES_PER_SAMPLE = 5
