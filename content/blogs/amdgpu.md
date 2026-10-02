+++
redirectTo = "/news/amdgpu"
date = "2018-05-22T00:00:00+10:00"
title = "Deep Learning without CUDA"
draft = false
type = "sidebar"
blog = true
stream = "news"

thumbnail = "/blogs/lecun.png"
summary = "Feel like the Deep Learning revolution is passing you by, because you have the wrong hardware? It seems like every Deep Learning software platform requires NVIDIA hardware running CUDA code. Well, I finally found one that doesn't! Let's see how it worked out."

authorname = "Hayim Dar"
authoravatar = "/people/HayimDar.jpg"
authorbio = "Works in in the Research Computing team, focussing on Artemis HPC, modelling and simulation."
+++

<figure>
<p align="center">
  <!-- <img src="/blogs/lecun.png" style="height:240px"> -->
  <figcaption><em>Image credit: Y LeCun 2016, adapted from Zeiler & Fergus 2013</em></figcaption>
  <br>
</p>
</figure>

Artificial Intelligence (AI) is the future -- and it has been since at least the Ancient Greek myth of [Talon](https://en.wikipedia.org/wiki/Talon), in which a giant bronze robot was built to protect the island of Crete. AI has definitely come a long way since then though, with the exponential increase in computing power offered by modern GPUs driving breakthroughs in the capability of modern neural networks.

If you're like me, you've probably wanted to get in on the action, and explore these networks for yourself. Artemis HPC [recently upgraded](/news/artemis_expansion/) to 108 (!) cutting-edge NVIDIA V100 GPU cards, of which 28 are available to general users. These cards are specially designed for _Deep Learning_, which is a method of structuring neural networks so that they can learn hierarchical representations of the data you input to them. Clear as mud?

You can simulate neural networks on Artemis using TensforFlow (set-up instructions [here](https://sydneyuni.atlassian.net/wiki/spaces/RC/pages/229114058/TensorFlow)). And look out for SIH's upcoming Artemis GPU and Deep Learning intro courses.


## Deep Learning @ home

But what if you just want to play a little first, before stepping up to HPC? If you have an _NVIDIA_ GPU in your desk- or laptop computer, you're in luck. All of the major Deep Learning packages work great on [CUDA](https://developer.nvidia.com/cuda-zone)-enabled (ie NVIDIA) chips: from the classic [Caffe](http://caffe.berkeleyvision.org/) to the more hip [TensorFlow](https://www.tensorflow.org/), a super popular 'back-end' for neural network simulation and which has extensive docs and [installation instructions](https://www.tensorflow.org/install/), and now developed by Google. With TensorFlow, you can also use the higher-level Deep Learning 'framework' [Keras](https://keras.io/), which automates a lot of the configuration required to initialise network models. Another popular engine, [PyTorch](https://pytorch.org/) also has extensive docs, or the adventurous reader could have a go of [MXNet](https://mxnet.apache.org/install/index.html) and its [Gluon](https://gluon-crash-course.mxnet.io/) framework.


<figure>
  <img src="/blogs/dl-frameworks.png" style="height:140px">
  <figcaption><em>There are a lot of options!</em></figcaption>
  <br>
</figure>

If, however, you have an _AMD_ GPU card, as I do in my University-provided 2017 Macbook Pro, then **none** of the above support your hardware, you have _very few_ options. In fact, until this blog post, I thought you had none. Enter PlaidML!

[PlaidML](http://vertex.ai/blog/announcing-plaidml) is another machine learning engine -- essentially a software library of neural network and other machine learning functions. Conveniently, PlaidML can be used as a back-end for Keras also. And, unlike basically every other such engine, PlaidML is designed for [OpenCL](https://www.khronos.org/opencl/), the poorer, open-source cousin of NVIDIA'S CUDA GPU programming language. Plus, it works on Macs. (PlaidML is Python based).

<img src="/blogs/plaid-final.png" style="height:120px">

### Getting PlaidML + AMD working on a Macbook Pro

The rest is actually pretty easy, here's what I did on a Macbook Pro (OSX High Sierra):

0. Ensure you have a decent Python environment installed.
   - [Anaconda](https://www.anaconda.com/download/) is the go-to; the stock Python that comes with OSX is generally not recommended.
1. Create a virtual environment using [conda](https://conda.io/docs/user-guide/tasks/manage-environments.html) (I've called mine 'plaidenv')

    ```
    conda create --name plaidenv
    source activate plaidenv
    ```

2. Install and configure PlaidML
    ```
    pip install -U plaidml-keras
    plaidml-setup
    ```
    You may be asked if you want to use 'experimental' devices -- my Macbook's Radeon Pro 560 is not officially supported, so say yes..
    ```
    ...
    Experimental Config Devices:
    llvm_preview_cpu.0 : LLVM_preview_CPU
    amd_radeon_pro_560_compute_engine.0 : AMD AMD Radeon Pro 560 Compute Engine
    intel(r)_hd_graphics_630.0 : Intel Inc. Intel(R) HD Graphics 630
    opencl_cpu.0 : Intel OpenCL CPU

    Using experimental devices can cause poor performance, crashes, and other nastiness.

    Enable experimental device support? (y,n)[n]: y

    ...

    Almost done. Multiplying some matrices...
    Tile code:
    function (B[X,Z], C[Z,Y]) -> (A) { A[x,y : X,Y] = +(B[x,z] * C[z,y]); }
    Whew. That worked.
    ```

#### So does it actually work?

To test this, I ran one of Keras' example codes, a standard [MNIST](http://yann.lecun.com/exdb/mnist/) handwritten-numerals classification task using convolutional neural nets, available [here](https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py). Using the default values, this network should learn to classify 28x28 pixel images of digits in the dataset to >99% accuracy. They also suggest that on an NVIDIA 'Grid K520' GPU, it should take ~ 16s for each training epoch, or 198s in total.

To get Keras to use PlaidML as its backend (and hence run any working Keras code), just add these lines **before** you import Keras:
```
# Install the plaidml backend
import plaidml.keras
plaidml.keras.install_backend()
```

So how did my laptop GPU do? Here are my results:

| Card | Specs | Training time |
|---|:---:|:---:|
| Core i7 CPU (Macbook Pro) | 8 threads, 16gb, 3.1GHz | ~ 4320s |
|**Radeon Pro 560 (Macbook Pro)** | 1024 cores, 4gb, 907 Mhz | 332s |
| NVIDIA K40 (Artemis) | 2888 cores, 12gb, 745 Mhz | 125 s |
| Grid M60 (Argus) | 2048 cores, 8gb, 930 Mhz | 115s |
| Artemis V100 (Artemis) | 5120 cores, 16gb, 1.5Ghz | 57s |

Firstly, it actually worked, which I thought was pretty impressive! Secondly, it was only 5x slower than the top-shelf V100s we have on Artemis. For comparison, I also tested it on one of our Argus Virtual Desktops, which don't perform too badly either.

Of course, for larger jobs requiring more RAM, my laptop GPU won't cut it. But for testing code and developing models? I's say Macbook users were now back in the game.

<p align="center">
<iframe src="https://giphy.com/embed/3o7qDS4hMV4hLWmGcw" width="260" height="257" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</p>

If you try this on your machine, [let me know](mailto:sih.training@sydney.edu.au) how it goes!
