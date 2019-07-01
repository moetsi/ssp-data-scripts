#!/usr/bin/env python3

import glob
import os
import sys

# struct FrameStruct {
#    unsigned short messageType;
#    std::vector<unsigned char> colorFrame;
#    std::vector<unsigned char> depthFrame;
#    std::string sceneDesc;
#    unsigned int sensorId;
#    unsigned int deviceId;
#    unsigned int frameId;
#    std::vector<unsigned long> timestamp;
#}

def parse_frame_folder(base_folder):
	# /home/amourao/data/nyc_depth/raw/basements/basement_0001a

	# d-1316653580.471513-1316138413.pgm
	# a-1316653580.475954-1316138413.dump
	# r-1316653580.484909-1316500621.ppm
	# d-1316653580.544897-1318140568.pgm
	# r-1316653580.552634-1318500909.ppm
	# a-1316653580.556176-1318500909.dump
	# d-1316653580.558266-1320142723.pgm
	pattern_color = os.path.join(base_folder, "r-*.ppm")
	pattern_depth = os.path.join(base_folder, "d-*.pgm")
	frames_color = sorted(glob.glob(pattern_color))
	frames_depth = sorted(glob.glob(pattern_depth))

	print(len(frames_color))
	
	for i, frame_color in enumerate(frames_color):
		time = float(frame_color.split("/")[-1].split("-")[1])
		depth_frame = min(frames_depth, key=lambda x:abs(float(x.split("/")[-1].split("-")[1]) - time))
		print("{};{};{}".format(i, frame_color, depth_frame))


def parse_metadata(base_folder, framerate):
	if base_folder.endswith("/"):
		base_folder = base_folder[:-1]

	sensorId = base_folder.split("/")[-1]
	sceneDesc = base_folder.split("/")[-2]
	
	sensorId = sensorId[-2:]

	sensorId = 0
	deviceId = 0
	print("ms_rgbd_7s_{};{};{};{}".format(sceneDesc, sensorId, deviceId, framerate))



def main(argv):
	if len(argv) < 3:
		print("Usage: generate_nyu_depth_filelist <path> <framerate>", file=sys.stderr)
	path = sys.argv[1]
	framerate = int(sys.argv[2])
	parse_metadata(path, framerate)
	parse_frame_folder(path)



if __name__ == "__main__":
	main(sys.argv)