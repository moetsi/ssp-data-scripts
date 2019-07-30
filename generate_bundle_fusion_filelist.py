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
	# "/home/amourao/data/bundle_fusion/apt0/frame-000000.color.jpg"
	# frame_id;color_frame_path
	pattern = os.path.join(base_folder, pattern)
	frames = sorted(glob.glob(pattern))
	print(len(frames))
	for i, frame in enumerate(frames):
		print("{};{}".format(i, frame))


def parse_metadata(base_folder, framerate, sensorId, frameType):
	sceneDesc = base_folder.split("/")[-1]
	
	if not sceneDesc:
		sceneDesc = base_folder.split("/")[-2]

	deviceId = 0
	print("bundle_fusion_{};{};{};{};{};".format(sceneDesc, deviceId, sensorId, frameType, framerate))



def main(argv):
	if len(argv) < 4:
		print("Usage: generate_bundle_fusion_filelist <path> <pattern> <framerate>", file=sys.stderr)
	path = sys.argv[1]
	pattern = sys.argv[2] # "frame-*.depth.png"
	framerate = int(sys.argv[3])
	
	if "color" in pattern:
		parse_metadata(path, framerate, 0, 0)
	else:
		parse_metadata(path, framerate, 1, 1)
	parse_frame_folder(path, pattern)



if __name__ == "__main__":
	main(sys.argv)