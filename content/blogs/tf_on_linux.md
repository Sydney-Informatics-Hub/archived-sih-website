+++
redirectTo = "/news/tf_on_linux"
date = "2019-01-15T00:00:00+10:00"
title = "Tensorflow on Ubuntu 18.04"
draft = false
type = "sidebar"
blog = true
stream = "news"

thumbnail = "/blogs/lecun.png"
summary = "How I installed Tensorflow on ubuntu Linux 18.04"

authorname = "Nathaniel Butterworth"
authoravatar = "/people/NathanielButterworth.jpg"
authorbio = "Works in in the Research Computing team, focussing on Artemis HPC, data vis and ice cream."
+++

Here is how I installed tensorflow on my Linux partition of a dual boot Dell Latitude 5490 with an internal NVIDIA GeForce MX130 GPU. All the specified versions are chosen for a reason, but other version combinations **might** work.

I installed Xubuntu 18.04

I updated and upgraded everything.

I switched to the nvidia-driver-390 (propietry,tested) under the Additional Drivers tab of the Xubuntu Software & Updates application.

I downloaded gcc-6 and g++6 and linked them as my main gcc/g++
```
sudo apt install gcc-6
sudo apt install g++-6
sudo rm /usr/bin/g++ (These were just soft links to
sudo rm /usr/bin/gcc
sudo ln -s /usr/bin/g++-6 /usr/bin/g++
sudo ln -s /usr/bin/gcc-6 /usr/bin/gcc
```

I downloaded the local runfile installer of CUDA 9.0 for Ubuntu 17.04 from here: 
https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1704&target_type=runfilelocal

I ran the runfile ensuring not to update the driver
```
sudo ./cuda_9.0.176_384.81_linux.run
```

I installed a few other packages
```
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
```

I installed cuDNN downloaded from here: 
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.4.2/prod/9.0_20181213/cudnn-9.0-linux-x64-v7.4.2.24.tgz
and then extracted.
```
sudo cp ~/Downloads/cuda/include/cudnn.h /usr/local/cuda-9.0/include/
cp ~/Downloads/cuda/include/cudnn.h /usr/local/cuda-9.0/include/
```

I made sure cuda libraries could be found
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-9.0/lib64/
```

I made a python conda environemt and installed tensorflow! 
```
conda create -n DL python=3.6
pip install tensorflow-gpu
```

Done.

The next step will be to use just the Intel UHD 620 for display and the NVIDIA  GeForce MX130 for compute.... (which I tried but have failed a few times). If you have done this on your machine successfully, [let me know](mailto:nathaniel.butterworth@sydney.edu.au) how it goes!







