---
title: Overview of CRBDD, the Coconut Rhinoceros Beetle Damage Detection Project
author: Aubrey Moore
date: 2026-10-25
updated: 2026-10-26
---

This blog post provides preliminary software documentation for CRBDD, the Coconut Rhinoceros Beetle Damage Detection Project.

## Background

The objective of CRBDD is to provide a standardized automated system for detecting coconut palms in digital images and for measuring the extent of coconut rhinoceros beetle (CRB), *Oryctes rhinoceros*, frrding damage to each detected palm.


Feeding damage is caused by CRB adults which bore into crowns to feed on sap. CRB grubs feed only on decaying plant material and do no damage. 
CRB adults are not true defoliators. Damage is caused to developing fronds inside the crown as the beetle bores through them on its way to the center of the crown to feed on sap.
The beetle feeds in the bore hole for only a few days and then leaves the tree.
When damaged fronds emerge from the crown and expand, several weeks later, distinctive v-shaped cuts become apparent and can be seen over a distance of several hundred meters.
V-shaped cuts remain visible until the frond senesces and falls off the palm after about 12 months.

Visual surveys of CRB damage have long been used for early detection of CRB in new geographic areas and to monitor changes over time and space, especially in response to control activities,
Prior to the advent of digital photography and geographic positioning systems, surveys were done by direct observation. These days, survey data are usually collected as georeferenced images.
In addition to planned surveys, many images available on the internet contain occurrences of healthy, damaged and dead coconut palms. 

The number of images containing one or more coconut palms available on the Internet is estimated to be [between tens of millions to at least hundreds of millions](https://share.google/aimode/ylKTq7S8nQJ8caRz9). And thousands more are added daily.

Much of the information in this blog post is available in [this screencast](https://doi.org/10.5281/zenodo.22984117).

## CRBDD Design Features

```{figure} images/images_for_crbdd/system_diagram1.svg
:label: crbdd_system_diagram
:align: left
System diagram.
```


* FOSS, See [](#crbdd_system_diagram).
* Python
* SAM3
* Spatialite database
* QGIS
* This blog article and future documentation will be written using [Myst markdown](https://mystmd.org/). 

## Details for Key Features

### Segment Anything Model (SAM3)

### SpatiaLite Database

See [](#my-mermaid-figure).

```{figure}
:label: my-mermaid-figure
:align: left
My nice figure.
```{mermaid}
erDiagram

    image {
        integer image_id PK "AUTOINCREMENT"
        text image_path "UNIQUE"
        integer image_width
        integer image_height
        text timestamp
        real meters_from_previous_location
        geometry location "POINT"
    }

    tree {
        integer tree_id PK "AUTOINCREMENT"
        integer image_id FK
        integer class_id
        real confidence
        integer tree_touches_edge "DEFAULT 0"
        integer shape_class
        integer soft_tree_class
        real soft_tree_prob
        text tree_class
        geometry tree_poly "POLYGON"
        real pixel_count "GENERATED ALWAYS AS (ST_Area(tree_poly)) VIRTUAL"
    }

    cut {
        integer cut_id PK "AUTOINCREMENT" 
        integer tree_id FK
        geometry cut_poly "POLYGON"
    }

    image ||--o{ tree : "contains"
    tree ||--o{ cut : "contains"
```



### SVG Images

## Workflow

### Inputs

### Outputs

## References

<!-- 
A recent trend in biocontrol research is to perform host specificity tests to
predict risk of unwanted nontarget affects impacts to species closely related to the target species, especially native species. In light of ongoing research on the use of *Oryctes rhinoceros* nudivirus (OrNV) isolates as effective self-sustainng biocontrol agents to suppress the Guam CRB population, I did a quick search for native species of Guam beetles closely related to CRB. 

The coconut rhinoceros beetle. *Oryctes rhinoceros*, is a species within the rhinoceros beetle subfamily, Dynastinae, and the scarab beetle family, Scarabaeidae.   

Dunlap et al. 2015[^1] listed 2 scarab beetles as native to Guam:

|Family|Subfamily|Tribe|Species|Author|Status|
|------|---------|-----|-------|------|------|
|Scarabaeidae|Aphodiinae|Eupariini|Ataenius yasumatsui|Nomura, 1943|native|
|Scarabaeidae|Melolonthinae|Melolonthini|Lepidiota carolinensis|(Arrow, 1939)|native|

However:
* Allsop[^2] claims that the record from Guam for *Holotrichia burmeistri*, a synonym of *Lepidiota carolinensis*, "is based on one individual in luggage". So this species should probably be dropped from the list as a being native to Guam (it is native to Palau).
* I could not find any Guam occurrence records for *Ataenius yasumatsui*. The GBIF accepted name for *Ataenius yasumatsui* is *Airapus interstitialis* and there is only [one occurrence record for this species in GBIF](https://www.gbif.org/occurrence/search?taxonKey=BD77) and this is from the Federated States of Micronesia. Occurrence status of this species on Guam requires further investigation.

Apparently there are no native beetle species "closely related" to CRB on Guam. That is good news because it reduces the risk of unwanted non-target effects. According to the current literature, OrNV attacks only rhinoceros beetles (subfamily Dynastinae).
Laboratory studies using hemocoel injection or forced inoculation have occasionally caused infection in other scarab species, but natural epizootics in the wild impact only target and near-target dynastine hosts.

However, if one wants to be overly cautious and test a Guam native beetle species which is not-so-closely related to CRB, Dunlap et al.[^1] list a candidate. It is a native stag beetle in the Lucanidae family which is part of the Scaraboidea superfamily. And it is quite common:

|Family|Subfamily|Tribe|Species|Author|Status|
|------|---------|-----|-------|------|------|
|Lucanidae|Lucaninae|Figulini|*Figulus integricollis*|Thomson, 1862|native|

In my opinion, this species is the Guam native beetle species most closely related to CRB.

[^1]:Dunlap, Joshua B., Mary Liz Jameson, Paul E. Skelley, Emmy L. Engasser, Amanda J. Redford. 2015. Scarab and Stag Beetles of Hawaii and the Pacific. USDA APHIS Identification Technology Program (ITP). Fort Collins, CO. Checklist last updated October 23, 2015.](https://idtools.org/scarab/files/Guam-Scarabaeoids-Checklist.pdf)


[^2]: Allsopp P G, Plazi (2025). Holotrichia burmeisteri Brenske, 1892 and allies (Coleoptera: Scarabaeidae: Melolonthinae: Rhizotrogini): a tale of four genera and four countries. Plazi.org taxonomic treatments database. Checklist dataset https://doi.org/10.15468/7k556a accessed via GBIF.org on 2026-08-11. 
-->