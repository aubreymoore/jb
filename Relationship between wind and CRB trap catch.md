---
title: Relationship between wind and CRB trap catch
subject: pheromone traps
# thumbnail: ./thumbnails/nice-image.png
date: 2025-12-31
authors:
  - name: Aubrey Moore
# exports:
#   - format: pdf
#     template: arxiv_two_column
#     output: exports/relationship_between_wind_and_CRB_trap_catch.pdf
---

```{figure} ./images/trap_catch_wind_sketch.jpg
:label: my-fig
:align: center
Expected relationship between wind and CRB pheromone trap catch.
```
Theoretically, CRB adults locate pheromone sources by flying across the wind until they detect a plume. 
At this point they turn upwind and follow the plume to its source.
Therefor, CRB pheromone traps which are upwind of a CRB population should be expected to catch more beetles than traps which are downwind.
This hypothesis may be tested using data stored in the Guam CRB trap catch database which contains data for about 2,000 georeferenced trap locations and about 90,000 trap visits.
Read-only access to this database is publicly available. See [Moore 2022](https://doi.org/10.5281/zenodo.7112147) for example queries using `python` and `SQL`.

[](#my-fig) is a sketch to help visualize my idea. Prevailing wind is from the NE.

The left side of the figure shows a trap line surrounding a port facility, an airfield in this case.
If we assume that the airfield is a poor source of CRB adults, it is expected that traps on the windward (NE) edge of the field will trap more beetles than those on the leeward (SW) edge.

The right side of the figure shows a trap line on the coast of an island.
If we assume that the ocean is a poor source of CRB adults, it is expected that traps on the windward (NE) edge of the island will trap less beetles than those on the leeward (SW) edge.

