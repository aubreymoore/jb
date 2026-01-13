---
title: EFD
subject: CRB damage
# thumbnail: ./thumbnails/nice-image.png
date: 2026-01-11
authors:
  - name: Aubrey Moore
bibliography:
  - references.bib
# exports:
#   - format: pdf
#     template: arxiv_two_column
#     output: exports/relationship_between_wind_and_CRB_trap_catch.pdf
---

# Literature search

Note: efd.py is in the sam3 folder.

Elliptical descriptors (EFD) seem to be a promising method for determining if coconut palms are damaged.
This page is the start of a search for relevent bibliographic references.

<https://doi.org/10.1016/0146-664X(82)90034-X> is a prime reference for EFD.

<https://doi.org/10.3390/fishes8040182> used EFD for automated identification of morphological characteristics of three *Thunnus* species based on different machine learning algorithms and compared results with othe ML methods. 

@tabugo2017 used EFD to differentiate seahorses in the Philippines.


# AI
____

START OF PERPLEXITY CHAT

provide a list of python libraries for elliptic Fourier descriptors with links

pyefd stands out as the primary Python library for computing elliptic Fourier descriptors from contours, supporting normalization for rotation and size invariance.

​

    pyefd: Install via pip install pyefd; computes descriptors using elliptic_fourier_descriptors(contour, order=10); GitHub at
    https://github.com/hbldh/pyefd
    ; docs at https://pyefd.readthedocs.io.

​

spatial-efd: Pure Python for spatial data like shapefiles; handles harmonics and plotting; requires numpy, matplotlib, pyshp; available at https://spatial-efd.readthedocs.io.

​

alessandroferrari/elliptic-fourier-descriptors: Fast NumPy/OpenCV implementation for binary images and shape reconstruction; GitHub at https://github.com/alessandroferrari/elliptic-fourier-descriptors.

    ​

These libraries integrate well with scikit-image or OpenCV for contour extraction, suiting computer vision workflows.

​
Related
Compare features of PyEFD and pyefd libraries
Show installation commands for each EFD Python package
Examples of reconstructing shapes from EFD coefficients
How to extract contours with OpenCV for EFD input
Which libraries support normalization and rotation invariance
Compare features of PyEFD and pyefd libraries

PyEFD and pyefd refer to the same Python library for elliptic Fourier descriptors, with PyEFD as its documented name and pyefd as the package/installation name.

​
Core Features

Both compute Fourier coefficients (a_n, b_n, c_n, d_n) from contours using elliptic_fourier_descriptors(contour, order=10), support normalization for rotation/size invariance via normalize=True or normalize_efd(), and integrate with OpenCV/scikit-image for contour input.

​
Key Functions
Function	Description	Parameters
elliptic_fourier_descriptors	Main function for EFD computation	contour (Nx2 array), order (int), normalize (bool), return_transformation (bool)
​
normalize_efd	Post-normalization of coefficients	coeffs (Nx4 array), size_invariant (bool), return_transformation (bool)
​
reconstruct_contour	Rebuilds contour from coefficients	coeffs, locus (A0/C0), num_points
​
plot_efd	Visualizes truncations (requires matplotlib)	coeffs, locus, image/contour optional
​
Usage Notes

Install via pip install pyefd; uses NumPy; tested with MNIST contours; features are typically coeffs.flatten()[3:] after normalization, ignoring first three fixed values. No distinct differences exist between "PyEFD" and "pyefd" beyond naming conventions in docs vs. PyPI.

​
How can I use knn to analyse pyefd results?

PyEFD outputs normalized elliptic Fourier descriptors as feature vectors suitable for k-NN classification after flattening coefficients (e.g., coeffs.flatten()[3:]).

​
Extract Features

Load contours, compute EFDs, and prepare features:

    Use normalize_efd(efd, size_invariant=True) for invariance.

    Flatten to 1D vector: features = np.array([normalize_efd(efd).flatten()[3:] for efd in efd_list]).

    Pair with labels: X = features; y = labels.

    ​

k-NN Implementation

Leverage scikit-learn for analysis:

text
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(accuracy_score(y_pred, y_test))

Cross-validate with cross_val_score(knn, X, y, cv=5); tune k via grid search.

​
Optimization Tips

Scale features if needed (StandardScaler); choose Euclidean or DTW metric for shape similarity; visualize with plot_efd for truncation order selection (e.g., 10-20 harmonics). This suits contour classification in computer vision tasks like pest shape analysis.

END OF PERPLECITY CHAT​
____

# Proposed workflow

1. Get a subset of polygons from the SQLite database for the Efate survey
2. Label the polygons.
3. Calculate normalized descriptors.
4. Analyze descriptors using knn or principal components

Note that steps 1 and 2 can be done using FiftyOne.


