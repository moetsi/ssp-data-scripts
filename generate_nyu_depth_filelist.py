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

def parse_frame_folder(base_folder, pattern):
	# /home/amourao/data/nyc_depth/raw/basements/basement_0001a

	# d-1316653580.471513-1316138413.pgm
	# a-1316653580.475954-1316138413.dump
	# r-1316653580.484909-1316500621.ppm
	# d-1316653580.544897-1318140568.pgm
	# r-1316653580.552634-1318500909.ppm
	# a-1316653580.556176-1318500909.dump
	# d-1316653580.558266-1320142723.pgm
	pattern_color = os.path.join(base_folder, pattern)
	frames_color = sorted(glob.glob(pattern_color))

	print(len(frames_color))
	
	for i, frame_color in enumerate(frames_color):
		print("{};{};{}".format(i, frame_color))


def parse_metadata(base_folder, framerate, sensorId, frameType):
	if base_folder.endswith("/"):
		base_folder = base_folder[:-1]

	deviceId = base_folder.split("/")[-1]
	sceneDesc = base_folder.split("/")[-2]
	
	print("ms_rgbd_7s_{};{};{};{};{}".format(sceneDesc, deviceId, sensorId, frameType, framerate))



def main(argv):
	if len(argv) < 4:
		print("Usage: generate_nyu_depth_filelist <path> <pattern> <framerate>", file=sys.stderr)
	path = sys.argv[1]
	pattern = sys.argv[2]
	framerate = int(sys.argv[3])
	if "r" in pattern:
		parse_metadata(path, framerate, 0, 0)
	else:
		parse_metadata(path, framerate, 1, 1)
	parse_frame_folder(path, pattern)



if __name__ == "__main__":
	main(sys.argv)