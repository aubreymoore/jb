---
title: Overview of CRBDD, the Coconut Rhinoceros Beetle Damage Detection Project
author: Aubrey Moore
date: 2026-10-25
---

## Background

Feeding damage to coconut palms is caused only by coconut rhinoceros beetles (CRB) adults, *Oryctes rhinoceros*, which bore into crowns to feed on sap.
They feed in the bore hole for only a few days and then leave the tree. CRB grubs feed only on decaying material and do no damage.
CRB adults are not true defoliators. Damage is caused to developing leaves inside the crown as the beetle bores through them on its way to the sap.
When damaged fronds emerge from the crown and expand, several weeks later, distinctive v-shaped cuts become apparent and can be seen over a distance of several hundred meters. 

Visual surveys of CRB damage have long been used for early detection of CRB in new geographic areas and to monitor changes over time and space, especially in response to control activities,
Prior to the advent of digital photography and geographic positioning systems, surveys were done by direct observation. These days, survey data are usually collected as georeferenced images.
In addition to planned surveys, many images available on the internet contain occurrences of healthy, damaged and dead coconut palms. 

The objective of CRBDD is to provide a standardized automated system for detecting coconut palms in digital images and for measuring the extent of damage to each detected palm.

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

## Details for Key Features

### Segment Anything Model (SAM3)

### SpatiaLite Database

```{figure} images/images_for_crbdd/test_db_erd.svg
:label: db_diagram
:align: left
Database diagram.
```
### SVG Images

## References

<!-- A recent trend in biocontrol research is to perform host specificity tests to
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


[^2]: Allsopp P G, Plazi (2025). Holotrichia burmeisteri Brenske, 1892 and allies (Coleoptera: Scarabaeidae: Melolonthinae: Rhizotrogini): a tale of four genera and four countries. Plazi.org taxonomic treatments database. Checklist dataset https://doi.org/10.15468/7k556a accessed via GBIF.org on 2026-08-11. -->