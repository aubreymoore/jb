---
title: Accessing CRB damage survey data shared via the Internet Archive
author: Aubrey Moore
date: 2026-07-14
---

I have added several CRB roadside damage survey datasets to the [Internet Archive](https://archive.org/).
Each archive contains a folder of high definition images (1920x1080 pixels).
Each image contains a timestamp and GPS coordinates embedded as [EXIF](https://en.wikipedia.org/wiki/Exif) metadata.

An entire dataset or individual items in a dataset can be easily downloaded using an [URL](https://en.wikipedia.org/wiki/URL).
Here is an example of an image fetched from the [Efate2025 dataset](https://archive.org/details/efate-2025) when you opened this page a few seconds ago:

![](https://ia903105.us.archive.org/view_archive.php?archive=/4/items/efate-2025/Efate2025.zip&file=crb%2F20251127_152140.jpg)

# Example URLS

## Get a list available CRB damage survey datasets
`https://archive.org/search?query=subject%3A%22images+from+a+roadside+survey+of+coconut+rhinoceros+beetle+damage%22`

[try it](https://archive.org/search?query=subject%3A%22images+from+a+roadside+survey+of+coconut+rhinoceros+beetle+damage%22)

## Get details for an individual dataset
`https://archive.org/details/efate-2025`

[try it](https://archive.org/details/efate-2025)

## Download a single image
`https://ia903105.us.archive.org/view_archive.php?archive=/4/items/efate-2025/Efate2025.zip&file=crb%2F20251127_152140.jpg`

[try it](https://ia903105.us.archive.org/view_archive.php?archive=/4/items/efate-2025/Efate2025.zip&file=crb%2F20251127_152140.jpg)

# Notes
- Alternate access to items in the Internet Archive is provided by a command line interface ([ia](https://archive.org/developers/internetarchive/cli.html)) and a Python library ([internetarchive](https://archive.org/developers/internetarchive/)).

# References
- [Are there download quotas for retrieving images from internet archive datasets?](https://share.google/aimode/Tn6PULwKE8rNZjSrG)
- [Is it possible to delete files and folders from an internet archive?](https://share.google/aimode/Gqc3LECRykXp9BQz1)