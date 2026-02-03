---
title: Evaluation of the SAM3 Model for detection of coconut palm trees in images
subject: sam3
date: 2026-01-31
authors:
  - name: Aubrey Moore
# exports:
#   - format: pdf
#     template: arxiv_two_column
#     output: exports/relationship_between_wind_and_CRB_trap_catch.pdf
---

This page evaluates SAM3, the most recent Segment Anything Model for automated detection of coconut palm trees.

Code associated with this page is available at https://github.com/aubreymoore/sam3-2026-01-31

We start by running SAM3 on two test images. 

The first image is simple. It comes from a NewYork Times article posted on the internet and it contains two coconut palms heavily damaged by coconut rhinoceros beetle (CRB). 

The second image is complex. It comes from a recent roadside survey of CRB damage on Efate Island in Vanuatu and it contains many coconut palms with various levels of damage.

```{figure} https://github.com/aubreymoore/sam3-2026-01-31/blob/main/08hs-palms-03-zglw-superJumbo.webp?raw=true
:label: nytimes
:alt: Sunset at the beach
:align: center

New York Times
```

```{figure} https://github.com/aubreymoore/sam3-2026-01-31/blob/main/20251129_152106.jpg?raw=true
:label: efate
:alt: Sunset at the beach
:align: center

Efate
```

```{figure} images/sam3-08hs-palms-03-zglw-superJumbo.jpg
:label: sam-nytimes
:align: center

New York Times
```

```{figure} images/sam3-20251129_152106.jpg
:label: sam-efate
:align: center

Efate
```




# References

:::{iframe} https://www.youtube.com/embed/BE2Nu3edyOo
:width: 100%
:align: center
:::