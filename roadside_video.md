---
title: Processing roadside imagery for CRB damage detection
subject: CRB damage
date: 2026-06-02
authors: Aubrey Moore
---

The purpose of this post is to share info on my attempts to improve detection of coconut rhinoceros beetle damage detection in roadside imagery.

I have been working on this project for quite awhile. Please have a look at this [YouTube recording](https://youtu.be/YLVTpX5MHys?t=7077) for background.

My new workflow uses these steps:

1. **Input** is a collection of roadside images which may or may not have metadata (timestamp, GPS coordinates, etc) embedded (in EXIF). Data may come from a variety of sources including automated roadside surveys, individual images, or web images publicly available on the WWW (social platforms, iNaturalist, etc.).
2. Coconut palms are detected in each image using the Segment Anything model (SAM3). This AI model requires no training and it does an excellent job of finding all coconut palms in an image, even dead ones ([related post](sam3.md)).
3. Each coconut palm detected in step 1. is examined for signs of CRB damage (v-shaped cuts etc.). I originally trained an AI model to do this step. But in this development cycle, I am using computer vision (CV) instead. My new method relies exclusively on shape analysis (visualized using binary masks).
4. **Output** is saved in a database which can be used to generate interactive web maps and statistical reports to monitor changes in CRB damage over space and time. 

Here's an initial test of the new workflow:

```{figure} https://github.com/aubreymoore/sam3-2026-01-31/blob/main/08hs-palms-03-zglw-superJumbo.webp?raw=true
:label: nytimes
A simple test image posted on the WWW by the New York Times.
```

```{figure} images/sam3-08hs-palms-03-zglw-superJumbo.jpg
:label: fig-sam-nytimes
SAM3 detection results from the simple image. This is the default annotated image returned by SAM3.
Numbers are confidence levels. SAM3 performed very well on this image, returning high confidence detections and precise segmentation even though the two coconut palms are heavily damaged.
```

```{figure} images/vcut_detections_0.png
:label: fig-workflow
This figure illustrates what happens when I apply my new computer vision workflow to the lefthand coconut palm detected by SAM3.
The `tree_mask` is a binary mask of the palm.
The `registered_mask` is a smooth version of the `tree_mask` reconstructed from elliptic Fourier descriptors.
The `additions_mask` shows the bitwise difference between the `tree_mask` and the `registered_mask`.
In the `overlaid_image`, the `additions_mask` is overlaid as red blogs. These are hardly visible because they are so small.

```

```{figure} images/vcut_detections.png
:label: fig-workflow-zoomed
This is a zoomed in version of ([](#fig-workflow)) to make it easier to see the red blobs in the `overlaid_image`.
Each blob represents an anomaly on the contour of the palm tree. In this case, most of them are v-shaped cuts symptomatic of CRB damage.
Note that the new workflow detects these features even though they are tiny. This suggests that the final workflow will be able to detect 
CRB damage to coconut palms anywhere in the image, not only to those in the foreground.
```
 ## References

 - [GPU requirements for large images](https://gemini.google.com/share/fd5d14f72e4d)
 - [GPU with largest memory available for free on Colab](https://share.google/aimode/bnRMn2XB9hJquuJOd)
 - [Sharing numpy arrays in a SpatiaLite DB](https://gemini.google.com/share/7f7283a4d82a)