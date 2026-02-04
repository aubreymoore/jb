---
title: Evaluation of the SAM3 model for detection of coconut palm trees in images
subject: sam3
date: 2026-02-04
authors:
  - name: Aubrey Moore
# exports:
#   - format: pdf
#     template: arxiv_two_column
#     output: exports/relationship_between_wind_and_CRB_trap_catch.pdf
---

# Introduction

This page documents my evaluation of SAM3, the most recent Segment Anything Model, for automated detection of coconut palm trees.

Code associated with this page is available at https://github.com/aubreymoore/sam3-2026-01-31

We start by running SAM3 on two test images:

- The first image ([](#nytimes))  is simple. It is from a NewYork Times article posted on the internet and it contains two coconut palms heavily damaged by coconut rhinoceros beetle (CRB). 
- The second image ([](#efate)) is complex. It is from a recent roadside survey of CRB damage on Efate Island in Vanuatu and it contains many coconut palms with various levels of damage.

```{figure} https://github.com/aubreymoore/sam3-2026-01-31/blob/main/08hs-palms-03-zglw-superJumbo.webp?raw=true
:label: nytimes
A simple test image posted on the internet by the New York Times.
```

```{figure} https://github.com/aubreymoore/sam3-2026-01-31/blob/main/20251129_152106.jpg?raw=true
:label: efate
A complex test image from a roadside coconut rhinoceros damage survey conducted on Efate Island, Vanuatu.
```

## SAM3 detection results for a simple image

SAM3 performed very well on this image, returning high confidence detections and precise segmentation even tough the two coconut palms were heavily damaged ([](#fig-sam-nytimes)).

```{figure} images/sam3-08hs-palms-03-zglw-superJumbo.jpg
:label: fig-sam-nytimes
SAM3 detection results from the simple image. This is the default annotated image returned by SAM3.
Numbers are confidence levels.
```
## SAM3 detection results for a complex image

SAM3 detected 25 coconut palms in this complex image. 
The default annotation image returned by SAM3 is too cluttered to be of much use,so I wrote my own code to display each detection separately.
The resulting images are displayed descending order of confidence.

A first look at these detections indicates that SAM3 does a remarkable job at detecting coconut palms in a complex image. 
It even finds dead standing stems without fronds and small objects.

There are no obvious false positive detections. However, a few detections include two or more coconut palms. 
Many of the segmentation masks are incomplete because palms are occluded by foreground objects.

```{figure} images/sam3-20251129_152106.jpg
:label: fig-sam-efate

SAM3 detection results from the complex image. This is the default annotation returned by SAM3.
Numbers are confidence levels.
```

## Detected object 02
confidence: 0.842 object_index: 16

![](images/images_for_sam3_post/20251129_152106.jpg-02.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-02.jpg)

## Detected object 03
confidence: 0.771 object_index: 5

![](images/images_for_sam3_post/20251129_152106.jpg-03.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-03.jpg)

## Detected object 04
confidence: 0.764 object_index: 9

![](images/images_for_sam3_post/20251129_152106.jpg-04.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-04.jpg)

## Detected object 05
confidence: 0.743 object_index: 3

![](images/images_for_sam3_post/20251129_152106.jpg-05.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-05.jpg)

## Detected object 06
confidence: 0.730 object_index: 12

![](images/images_for_sam3_post/20251129_152106.jpg-06.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-06.jpg)

## Detected object 07
confidence: 0.699 object_index: 2

![](images/images_for_sam3_post/20251129_152106.jpg-07.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-07.jpg)

## Detected object 08
confidence: 0.691 object_index: 20

![](images/images_for_sam3_post/20251129_152106.jpg-08.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-08.jpg)

## Detected object 09
confidence: 0.678 object_index: 7

![](images/images_for_sam3_post/20251129_152106.jpg-09.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-09.jpg)

## Detected object 10
confidence: 0.650 object_index: 0

![](images/images_for_sam3_post/20251129_152106.jpg-10.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-10.jpg)

## Detected object 11
confidence: 0.630 object_index: 24

![](images/images_for_sam3_post/20251129_152106.jpg-11.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-11.jpg)

## Detected object 12
confidence: 0.616 object_index: 8

![](images/images_for_sam3_post/20251129_152106.jpg-12.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-12.jpg)

## Detected object 13
confidence: 0.568 object_index: 22

![](images/images_for_sam3_post/20251129_152106.jpg-13.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-13.jpg)

## Detected object 14
confidence: 0.535 object_index: 15

![](images/images_for_sam3_post/20251129_152106.jpg-14.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-14.jpg)

## Detected object 15
confidence: 0.511 object_index: 14

![](images/images_for_sam3_post/20251129_152106.jpg-15.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-15.jpg)

## Detected object 16
confidence: 0.480 object_index: 4

![](images/images_for_sam3_post/20251129_152106.jpg-16.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-16.jpg)

## Detected object 17
confidence: 0.470 object_index: 11

![](images/images_for_sam3_post/20251129_152106.jpg-17.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-17.jpg)

## Detected object 18
confidence: 0.458 object_index: 10

![](images/images_for_sam3_post/20251129_152106.jpg-18.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-18.jpg)

## Detected object 19
confidence: 0.412 object_index: 21

![](images/images_for_sam3_post/20251129_152106.jpg-19.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-19.jpg)

## Detected object 20
confidence: 0.402 object_index: 19

![](images/images_for_sam3_post/20251129_152106.jpg-20.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-20.jpg)

## Detected object 21
confidence: 0.397 object_index: 23

![](images/images_for_sam3_post/20251129_152106.jpg-21.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-21.jpg)

## Detected object 22
confidence: 0.348 object_index: 6

![](images/images_for_sam3_post/20251129_152106.jpg-22.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-22.jpg)

## Detected object 23
confidence: 0.344 object_index: 18

![](images/images_for_sam3_post/20251129_152106.jpg-23.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-23.jpg)

## Detected object 24
confidence: 0.320 object_index: 13

![](images/images_for_sam3_post/20251129_152106.jpg-24.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-24.jpg)

## Detected object 25
confidence: 0.281 object_index: 17

![](images/images_for_sam3_post/20251129_152106.jpg-25.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-25.jpg)

## Detected object 26
confidence: 0.260 object_index: 1

![](images/images_for_sam3_post/20251129_152106.jpg-26.jpg)

![](images/images_for_sam3_post/roi-20251129_152106.jpg-26.jpg)



# References

:::{iframe} https://www.youtube.com/embed/BE2Nu3edyOo
:width: 100%
:align: center
:::