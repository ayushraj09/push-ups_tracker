# Push-Up Tracker 💪

A real-time push-up counter and posture analyzer using computer vision and pose estimation. This project uses MediaPipe and OpenCV to track your push-up form and automatically count repetitions while providing feedback on your posture.

## Features

- **Real-time Push-up Counting**: Automatically counts push-ups based on elbow angle analysis
- **Posture Analysis**: Monitors knee and back alignment to ensure proper form
- **Visual Feedback**: 
  - Live pose landmarks overlay
  - Good/Bad posture indicators
  - Real-time rep counter
  - FPS display
- **Computer Vision Based**: No wearable sensors required - works with just a webcam

## Demo

The application displays:
- Live video feed with pose estimation
- Push-up count in real-time
- Posture feedback (Good/Bad Posture)
- Frame rate information

## Requirements

```
opencv-python>=4.5.0
mediapipe>=0.8.0
numpy>=1.21.0
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/push-up-tracker.git
cd push-up-tracker
```

2. Install required dependencies:
```bash
pip install opencv-python mediapipe numpy
```

3. Run the application:
```bash
python push_up_tracker.py
```

## Usage

1. **Setup**: Position yourself in front of your webcam in a push-up starting position
2. **Positioning**: Ensure your full body is visible in the camera frame
3. **Start Exercising**: Begin doing push-ups - the counter will automatically track your reps
4. **Monitor Form**: Watch for "Good Posture" vs "Bad Posture" feedback
5. **Exit**: Press any key to quit the application

### Optimal Camera Setup
- Position camera at ground level or slightly elevated
- Ensure good lighting
- Keep entire body visible in frame
- Side view works best for accurate angle measurement

## How It Works

### Pose Detection
The system uses MediaPipe's pose estimation to identify 33 key body landmarks in real-time.

### Push-up Detection Algorithm
1. **Elbow Angle Analysis**: Monitors the angle between shoulder, elbow, and wrist (landmarks 12-14-16)
2. **Range Mapping**: Maps elbow angles from 75° to 160° to a 0-100% range
3. **Rep Counting**: Counts a full repetition when transitioning from 100% (top) to 0% (bottom) and back

### Posture Analysis
- **Knee Alignment**: Checks if knee angle (landmarks 12-24-26) stays between 170°-190°
- **Back Straightness**: Monitors back angle (landmarks 24-26-28) for proper alignment
- **Real-time Feedback**: Displays "Good Posture" when both conditions are met

## File Structure

```
push-up-tracker/
│
├── pose_estimation_module.py    # Core pose detection class
├── push_up_tracker.py          # Main application
└── README.md                   # This file
```

## Technical Details

### Key Components

**PoseDetector Class** (`pose_estimation_module.py`):
- `findPose()`: Detects and draws pose landmarks
- `findPosition()`: Extracts landmark coordinates
- `findAngle()`: Calculates angles between three points

**Main Tracker** (`push_up_tracker.py`):
- Real-time video processing
- Push-up counting logic
- Posture evaluation
- UI overlay management

### MediaPipe Landmarks Used
- **12**: Left Shoulder
- **14**: Left Elbow  
- **16**: Left Wrist
- **24**: Left Hip
- **26**: Left Knee
- **28**: Left Ankle

## Customization

### Adjusting Sensitivity
Modify these values in `push_up_tracker.py`:

```python
# Elbow angle range for push-up detection
per = np.interp(elbow, (75, 160), (0, 100))

# Posture angle thresholds
if knee > 170 and knee < 190:  # Knee alignment
if back > 170 and back < 190:  # Back straightness
```

### Detection Confidence
Adjust in `pose_estimation_module.py`:
```python
detector = PoseDetector(detectionCon=0.7, trackCon=0.7)  # Higher = more strict
```

## Limitations

- Works best with side-view camera angle
- Requires good lighting conditions
- Single person detection only for better accuracy
- Left-side body landmarks used (assumes left side visible)
- May need calibration for different body types

## Troubleshooting

**Camera not detected:**
- Check if camera is properly connected
- Try changing camera index in `cv.VideoCapture(0)` to `cv.VideoCapture(1)`

**Inaccurate counting:**
- Ensure proper camera positioning
- Check lighting conditions
- Verify full body is visible in frame
- Adjust angle thresholds if needed

**Poor pose detection:**
- Improve lighting
- Wear contrasting clothing
- Ensure clear background
- Check camera resolution

## Future Enhancements

- [ ] Multiple exercise support (squats, lunges, etc.)
- [ ] Exercise session logging
- [ ] Audio feedback

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for pose estimation
- [OpenCV](https://opencv.org/) for computer vision capabilities
- Computer Vision community for inspiration and resources

---

**Note**: This is a fitness tracking tool and should not replace professional fitness guidance. Always consult with fitness professionals for proper form and exercise recommendations.
