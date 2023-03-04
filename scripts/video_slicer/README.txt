------------
File Structure:

input_vid/ -- where you put your video pending to be sliced
Example file format:
<racetrack_name>_pov_<year>_<sportseries>_<firstname>_<lastname>.mp4
out/ -- the output images will be generated here under a folder having the same name as the video

------------
Example Usage:

In the root folder of this package, run `python3 video_slicer.py <video_filename>.mp4 <frame_interval>`

For example, 'python3 video_slicer.py input_vid/monza_pov_2022_f1_guanyu_zhou.mp4 100'
