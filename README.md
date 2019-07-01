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

For a single scene, the process works as follow:

```
wget http://graphics.stanford.edu/projects/bundlefusion/data/apt0/apt0.zip
unzip apt0.zip
```

Run the following command on the davp folder:

```
python generate_bundle_fusion_filelist.py /home/amourao/data/bundle_fusion/apt0/ 30 > apt0-frames.txt
```

The full list of datasets is available below:

```
https://graphics.stanford.edu/projects/bundlefusion/data/apt0/apt0.zip
https://graphics.stanford.edu/projects/bundlefusion/data/apt1/apt1.zip
https://graphics.stanford.edu/projects/bundlefusion/data/apt2/apt2.zip
https://graphics.stanford.edu/projects/bundlefusion/data/copyroom/copyroom.zip
https://graphics.stanford.edu/projects/bundlefusion/data/office0/office0.zip
https://graphics.stanford.edu/projects/bundlefusion/data/office1/office1.zip
https://graphics.stanford.edu/projects/bundlefusion/data/office2/office2.zip
https://graphics.stanford.edu/projects/bundlefusion/data/office3/office3.zip
```

### MS RGB-D Dataset 7-Scenes 

The generate_ms_rgbd_7s_filelist is a python script that reads frame metadata and generates a streaming ready frame list file.


```
wget http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/stairs.zip
unzip stairs.zip
```

```
python generate_ms_rgbd_7s_filelist.py /home/amourao/data/ms_rgbd_7s/stairs/seq-01/ 30 > stairs-seq-01-frames.txt
```


The full list of datasets is available below:

```
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/chess.zip
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/fire.zip
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/heads.zip
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/office.zip
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/pumpkin.zip
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/redkitchen.zip
http://download.microsoft.com/download/2/8/5/28564B23-0828-408F-8631-23B1EFF1DAC8/stairs.zip
```