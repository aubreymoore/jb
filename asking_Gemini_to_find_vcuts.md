--- 
title: Asking Gemini to find vcuts
subject: CRB damage
date: 2026-04-17
authors:
  - name: Aubrey Moore
--- 

# Asking Gemini to write code to find vcuts

Gemini continues to blow my mind.

I submitted the following prompt to Gemini Pro 3.1.

I am developing python code to find damage to coconut palms caused by coconut rhinoceros beetles which cause distinctive v-shaped cuts to fronds. These can be modeled as convexity hull defects in the crowns of coconut palms.  I am starting with a binary segmentation mask for a badly damaged coconut palm. I want to follow these steps: 1. Cut the mask into two parts: crown and trunk. 2. Enclose the crown in a convex hull and find convexity defects. 3. Visualize results.  Please provide two python code examples which perform these steps. Use opencv for the first example and scikit-image for the second example.

Here is the response from Gemini with the code it wrote for me transcribed into a [Jupyter notebook](https://nbviewer.org/github/aubreymoore/cv2_ski/blob/main/cv2_ski.ipynb).

And here's an updated version of the same [Jupyter notebook after a few fixes and improvements](https://nbviewer.org/github/aubreymoore/cv2_ski_fixed/blob/main/cv2_ski.ipynb).

## Results

Gemini did an amazing job considering the complexity of my prompt. Two python code examples for finding and visualizing v-shaped cuts in coconut palms were returned as requested. Gemini also returned a function which generates a synthetic binary mask of a palm with V-shaped cuts. Generation of synthetic data was not mentioned in my prompt. Both code examples executed without modification.

## Comments on code for Method 1: Using OpenCV

When I ran the code "out of the box",
the figure showed an obvious problem which is easy to fix. The simulated v-shaped cuts are too deep, cutting the crown into two segments.

The code uses the standard convexity hull defects algorithm.

## Comments on code for Method 2: Using Scikit-Image

Works as expected without any changes.

The code does not use the standard convexity hull defects algorithm. Instead, it generates a convex hull image and subtracts the original mask from it. The remaining pixels represent the "empty space" or defects. This is a much simpler algorithm and a lot more general. The defects are no longer constrained to being triangles as they are in the first method.

## General comments

Gemini and other AIs are great learning tools, but only if my prompts ask the right questions.

Gemini suggested a much better approach for detecting v-shaped cuts than the standard convexity hull defects method I have been using. In addition, it looks like scikit-image might be a better python package than opencv for geometric morphometrics.