#!/bin/bash

#H264: The range of the CRF scale is 0–51, where 0 is lossless, 23 is the default, and 51 is worst quality possible. A lower value generally leads to higher quality, and a subjectively sane range is 17–28. Consider 17 or 18 to be visually lossless or nearly so; it should look the same or nearly the same as the input but it isn't technically lossless.
#H264: The range is exponential, so increasing the CRF value +6 results in roughly half the bitrate / file size, while -6 leads to roughly twice the bitrate. 

#H265: The default is 28, and it should visually correspond to libx264 video at CRF 23, but result in about half the file size. Other than that, CRF works just like in x264. 

mkdir -p videos

folders='chess fire heads office pumpkin redkitchen stairs'
crfs264='17 23 29'
crfs265='22 28 34'

for folder in $folders
do
	for seqnum in $(seq -f "%02g" 1 15)
	do
		for crf in $crfs264
		do
			ffmpeg -threads 4 -framerate 30 -pattern_type glob -i "$folder/seq-$seqnum/*.depth.png" -crf $crf videos/$folder.$seqnum.depth-h264-$crf.mp4
			ffmpeg -threads 4 -framerate 30 -pattern_type glob -i "$folder/seq-$seqnum/*.color.png" -crf $crf videos/$folder.$seqnum.color-h264-$crf.mp4
		done
		for crf in $crfs265
		do
			ffmpeg -threads 4 -framerate 30 -pattern_type glob -i "$folder/seq-$seqnum/*.depth.png" -vcodec libx265 -crf $crf videos/$folder.$seqnum.depth-h265-$crf.mp4
			ffmpeg -threads 4 -framerate 30 -pattern_type glob -i "$folder/seq-$seqnum/*.color.png" -vcodec libx265 -crf $crf videos/$folder.$seqnum.color-h265-$crf.mp4
		done			
	done			
done
