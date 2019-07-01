# DAVP Data Scripts

This repo deals with processing data from existing datasets for DAVP processing.

## DAVP Frame Format

The DAVP frame format was created to be compatible with existing RGB-D datasets with separate RGB and depth frames-
It has the following structure:

```
<dataset name>;<device id>;<sensor id>;<fps>
<number of frames>
<frame id>;<color frame path>;<color frame path>
<frame id>;<color frame path>;<color frame path>
<frame id>;<color frame path>;<color frame path>
....
```

Example:

```
bundle_fusion_apt0;0;0;30
8560
0;/home/amourao/data/bundle_fusion/apt0/frame-000000.color.jpg;/home/amourao/data/bundle_fusion/apt0/frame-000000.depth.png
1;/home/amourao/data/bundle_fusion/apt0/frame-000001.color.jpg;/home/amourao/data/bundle_fusion/apt0/frame-000001.depth.png
....
```


## Datasets

### Bundle Fusion

The generate_bundle_fusion_filelist is a python script that reads frame metadata and generates a streaming ready frame list file.

```
generate_bundle_fusion_filelist.py <path to extracted bundle_fusion folder> <desired streaming framerate>
```

```
wget http://graphics.stanford.edu/projects/bundlefusion/data/apt0/apt0.zip
unzip apt0.zip
```

For example, run the following command on the davp folder:

```
python generate_bundle_fusion_filelist.py /home/amourao/data/bundle_fusion/apt0/ 30 > apt0-frames.txt
```
