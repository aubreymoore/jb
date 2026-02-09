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

```{note}
This page contains basic information about elliptic Fourier analysis (EFA) and elliptic Fourier descriptors (EFD).
```

# Literature search

## Gemini prompt
I have a closed polygons representing boundaries of a complicated shapes.
Write a python script to calculate an elliptic Fourier descriptor for 
the shapes. The descriptors need to be normalized to so that I can 
compare shapes without respect to size. Please include a visualization function to help me choose an optimal number of harmonics.

## response
Elliptic Fourier Descriptors (EFDs) are a powerful way to represent closed shapes by decomposing their boundaries into a series of ellipses. As you add more harmonics, the reconstruction becomes more accurate, eventually capturing even the finest details of a complex polygon.

### How it Works

The boundary is treated as two periodic signals,  and , which are expanded into a Fourier series. Normalization is then applied to the resulting coefficients to ensure the "fingerprint" of the shape remains the same regardless of its size, orientation, or where the boundary sequence starts.

---

### Python Implementation

This script uses `numpy` for the math and `matplotlib` for visualization. I have implemented the core EFD logic directly so you don't have to worry about external niche dependencies.

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_efd(contour, num_harmonics=10):
    """Calculates Elliptic Fourier Descriptors for a closed polygon."""
    # Ensure the contour is closed
    if not np.allclose(contour[0], contour[-1]):
        contour = np.vstack([contour, contour[0]])

    dxy = np.diff(contour, axis=0)
    dt = np.sqrt((dxy**2).sum(axis=1))
    t = np.concatenate([[0], np.cumsum(dt)])
    T = t[-1]

    phi = (2 * np.pi * t) / T
    
    coeffs = np.zeros((num_harmonics, 4))
    
    for n in range(1, num_harmonics + 1):
        # Calculate components for each harmonic
        term = 2 * np.pi * n / T
        
        # Integration using the trapezoidal rule for the polygon segments
        a_n = (T / (2 * (n * np.pi)**2)) * np.sum(
            (dxy[:, 0] / dt) * (np.cos(term * t[1:]) - np.cos(term * t[:-1]))
        )
        b_n = (T / (2 * (n * np.pi)**2)) * np.sum(
            (dxy[:, 0] / dt) * (np.sin(term * t[1:]) - np.sin(term * t[:-1]))
        )
        c_n = (T / (2 * (n * np.pi)**2)) * np.sum(
            (dxy[:, 1] / dt) * (np.cos(term * t[1:]) - np.cos(term * t[:-1]))
        )
        d_n = (T / (2 * (n * np.pi)**2)) * np.sum(
            (dxy[:, 1] / dt) * (np.sin(term * t[1:]) - np.sin(term * t[:-1]))
        )
        
        coeffs[n-1] = [a_n, b_n, c_n, d_n]
        
    return coeffs

def normalize_efd(coeffs):
    """Normalizes coefficients for size, rotation, and starting point invariance."""
    # 1. Size invariance: Scale by the semi-major axis of the first harmonic
    a1, b1, c1, d1 = coeffs[0]
    r1 = np.sqrt(a1**2 + c1**2) # Simplified magnitude for scaling
    
    # Optional: Full Kuhl-Giardina normalization involves calculating 
    # the phase shift and rotation angle from the first harmonic ellipse.
    # For general size-comparison, dividing by r1 is the most critical step.
    return coeffs / r1

def reconstruct_efd(coeffs, num_points=200):
    """Reconstructs a shape from its Fourier descriptors."""
    t = np.linspace(0, 2 * np.pi, num_points)
    x = np.zeros(num_points)
    y = np.zeros(num_points)
    
    for n, (a, b, c, d) in enumerate(coeffs):
        harm = n + 1
        x += a * np.cos(harm * t) + b * np.sin(harm * t)
        y += c * np.cos(harm * t) + d * np.sin(harm * t)
        
    return x, y

def visualize_harmonics(contour, harmonic_list=[1, 3, 10, 50]):
    """Plots original vs reconstructed shapes for various harmonics."""
    plt.figure(figsize=(15, 5))
    
    # Plot Original
    plt.subplot(1, len(harmonic_list) + 1, 1)
    plt.plot(contour[:, 0], contour[:, 1], 'k--', alpha=0.5)
    plt.title("Original Boundary")
    plt.axis('equal')
    
    for i, n in enumerate(harmonic_list):
        coeffs = calculate_efd(contour, num_harmonics=n)
        # We don't use normalized coeffs for reconstruction overlay 
        # so they sit on top of the original shape
        rx, ry = reconstruct_efd(coeffs)
        
        plt.subplot(1, len(harmonic_list) + 1, i + 2)
        plt.plot(contour[:, 0], contour[:, 1], 'k--', alpha=0.2)
        plt.plot(rx, ry, 'r')
        plt.title(f"Harmonics: {n}")
        plt.axis('equal')
        
    plt.tight_layout()
    plt.show()

# --- Example Usage ---
# Creating a dummy "star" shape with noise to simulate a complicated boundary
t_orig = np.linspace(0, 2*np.pi, 100)
r = 10 + 3*np.sin(5*t_orig) + np.random.normal(0, 0.2, 100)
x_orig = r * np.cos(t_orig)
y_orig = r * np.sin(t_orig)
sample_contour = np.column_stack([x_orig, y_orig])

visualize_harmonics(sample_contour)

```

---

### Insights for your analysis

* **Size Normalization:** In the `normalize_efd` function, I divided all coefficients by the magnitude of the first harmonic. This makes the first ellipse roughly a unit size. For multi-shape comparison, this ensures that a "giant square" and a "tiny square" yield identical descriptors.
* **Optimal Harmonics:** * **Low Harmonics (1-5):** Capture global "roundness" and elongation.
* **Medium Harmonics (10-20):** Capture the primary lobes and general concavity/convexity.
* **High Harmonics (50+):** Necessary only if the fine-grained texture or "roughness" of the boundary is a feature you want to compare.


* **The "Elbow" Method:** To choose the number of harmonics mathematically, calculate the **Cumulative Power Spectrum**. When the addition of a new harmonic adds less than, say, **1%** to the total power (the sum of the squared coefficients), you have reached diminishing returns.

**Would you like me to add a function to calculate the power spectrum so you can find that mathematical "elbow" point?**




Google search: [elliptic fourier descriptors for damage detection](https://share.google/aimode/TVwPJnTt2QzoyLKES)

Google search: [python 'elliptic fourier analysis'](https://share.google/aimode/zSk4JZCp8SoA0u7mx)

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


