---
subject: CRB pheromone simulation
# thumbnail: ./thumbnails/nice-image.png
date: 2026-04-17
authors:
  - name: Aubrey Moore
# bibliography:
#   - references.bib
exports:
  - format: pdf
    template: arxiv_two_column
    output: exports/crb_refs.pdf
---

# Simulation of CRB response to pheromone sources

I am thinking of putting together a simulation of CRB response to pheromone sources.
I will probably use NetLogo for an agent-based sim.

Started out with a Gemini query.

## Gemini prompt

NetLogo simulation model of moth navigating to a pheromone source

## Gemini response

A NetLogo simulation of a [moth](https://www.google.com/search?kgmid=/m/0hlhl&q=netlogo+simulation+model+of+a+moth+navigating+to+a+pheromone+source) navigating to a pheromone source typically models anemotaxis (wind-directed movement) combined with chemotaxis (chemical sensing). Because pheromone plumes in nature are turbulent and filamentous rather than smooth gradients, moths use a "surge and cast" strategy: they surge upwind when they detect pheromone and "cast" (zigzag crosswind) when they lose the signal. [1, 2, 3, 4] 
Below is a logic-based framework and code structure for building this model in NetLogo.
### 🧪 Core Simulation Logic

   1. Pheromone Dispersion: Pheromone is released from a source and moves with the wind. It is best modeled using patches that "diffuse" and "evaporate" or by using moving "scent" particles.
   2. [Moth](https://www.google.com/search?kgmid=/m/0hlhl&q=netlogo+simulation+model+of+a+moth+navigating+to+a+pheromone+source) States:
   * Surging: Moving directly upwind (180° away from the wind direction) upon detecting pheromone.
      * Casting: Zigzagging crosswind (roughly 90° to the wind) to re-acquire a lost scent.
      * Ranging: Random flight used before any pheromone is detected. [2, 4, 5, 6, 7] 
   
------------------------------
### 💻 NetLogo Model Code Structure

```
globals [ wind-direction ] ; e.g., 0 (North), 90 (East), etc.
patches-own [ pheromone ]

to setup
  clear-all
  set wind-direction 90 ; Wind blowing from West to East
  setup-patches
  setup-moths
  reset-ticks
end

to setup-patches
  ask patch (min-pxcor) 0 [ set pheromone 100 ] ; Pheromone source
  ask patches [ set pcolor scale-color white pheromone 0 50 ]
end

to setup-moths
  create-turtles 1 [
    set color yellow
    set xcor max-pxcor - 5 ; Start downwind
    set ycor 0
  ]
end

to go
  diffuse-pheromone
  ask turtles [ navigate ]
  tick
end

to diffuse-pheromone
  ask patches [
    ; Wind effect: Move pheromone toward wind-direction
    set pheromone pheromone * 0.9 ; Evaporation
    let target patch-at-heading-and-distance wind-direction 1
    if target != nobody [
      ask target [ set pheromone pheromone + ([pheromone] of myself * 0.1) ]
    ]
  ]
  ask patches [ set pcolor scale-color white pheromone 0 50 ]
end

to navigate
  ifelse pheromone > 0.1 [
    ; SURGE: Fly upwind (opposite of wind-direction)
    set heading wind-direction + 180
    fd 0.5
  ] [
    ; CAST: Zigzag crosswind to find the plume again
    rt (random 60 - 30)
    fd 0.3
  ]
end
```
------------------------------
### 🛠️ Advanced Features to Add

* Turbulence: Instead of a smooth diffusion, add random "puffs" of pheromone that move with the wind to simulate the intermittent nature of real plumes.
* Sensory Thresholds: Set a specific pheromone-threshold slider. Moths only respond if pheromone > threshold.
* Optomotor Anemotaxis: Real moths use visual cues to determine wind direction. In NetLogo, this is simplified by letting the turtle "know" the wind-direction global variable.
* Success Metrics: Use BehaviorSpace to track the mean first arrival time or the success rate of moths reaching the source under different wind speeds. [2, 4, 8, 9] 

### 💡 Probing Questions
To help you refine this model, consider:

* Do you want the wind to be constant, or should it change direction (meandering) over time?
* Should the pheromone be a continuous field (like a gradient) or discrete "puffs" that disappear?
* Are you modeling a single moth or a population competing to reach the source first? [4] 


[1] [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720835/)

[2] [https://journals.plos.org](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0198422)

[3] [https://www.researchgate.net](https://www.researchgate.net/publication/312213644_Moth_Navigation_along_Pheromone_Plumes)

[4] [https://academicweb.nd.edu](https://academicweb.nd.edu/~alindsa1/Publications/mothFinal.pdf)

[5] [https://www.researchgate.net](https://www.researchgate.net/publication/312213644_Moth_Navigation_along_Pheromone_Plumes)

[6] [https://stackoverflow.com](https://stackoverflow.com/questions/34598682/use-patches-diffusion-in-netlogo)

[7] [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7613704/#:~:text=Overview%20over%20the%20odor%20plume%20experiment.%20A:,sensor%20and%201%20into%20maximal%20sensory%20input.)

[8] [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC5999112/)

[9] [https://www.scitepress.org](https://www.scitepress.org/Papers/2024/127688/127688.pdf)
