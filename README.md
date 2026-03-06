

Quickstart for Hydrogenic Orbital PyViewer


Hydrogenic Orbital PyViewer is a Graphical User Interface (GUI)-based atomic orbital visualization tool. It aims to intuitively display function graphs related to atomic orbitals—such as radial wave functions, spherical harmonic functions, and wave function isosurfaces—through line plots, 2D plots, and 3D plots. This tool helps users understand the mathematical characteristics of atomic orbitals

1. Download and Install Python
If Python is already installed on your computer, skip to Step 2. Otherwise:
Option 1 (Recommended) : Use the Python installer provided by us.
Option 2: Download a compatible version from the https://www.python.org/downloads/.
Select the installer matching your operating system (Windows/macOS/Linux).
During installation:
Check the box Add Python to PATH and proceed with default settings by clicking Install Now. Proceed with default settings by clicking Next and Close when finished.
 
Note: If errors occur later, reinstall using our provided Python installer to ensure compatibility.

2. Install Required Libraries
If libraries like numpy, PyQt5, matplotlib, traits, VTK, and mayavi are already installed, skip to Step 3. Otherwise:
If you used our Python installer:
Run Requirements.bat (double-click the file).
If you used another Python version:
First try running Requirements.bat.
If errors occur, manually install dependencies using:
pip install numpy PyQt5 matplotlib traits vtk mayavi

3. Run Hydrogenic Orbital PyViewer
Locate the main.py file.
Right-click it and select Edit with IDLE (Python’s built-in IDE)
In the IDLE menu bar, go to Run → Run Module (or press F5).
The program interface will launch in a new window. Please note that the first run may take about several minutes or so.
 
The program's main interface is divided into two core areas with a clear layout and simple operation:
Left: Image Type Selection Panel
Contains 3 buttons for selecting the type of image to generate:
Line Plot : Displays 1D function curves (e.g., radial wave functions).
2D Plot : Displays 2D planar function distributions (e.g., spherical harmonics projections).
3D Plot : Displays 3D spatial function distributions (e.g., wave function isosurfaces)
Right: Function Selection Panel
Dynamically updates based on the image type selected on the left. Displays specific function options for the chosen plot type (e.g., orbital wave functions, probability densities).
Users first select the visualization dimension (1D/2D/3D) → then choose target functions.
Key Troubleshooting Tips
Python PATH issues: Reinstall Python and ensure Add Python to PATH is checked
Library errors: Use pip install --upgrade [library_name] to update problematic packages.
IDLE not found: Verify Python installation or launch main.py via command line: python main.py
This guide prioritizes clarity and compatibility. For advanced setups (e.g., virtual environments), refer to official Python documentation

4. Display Orbitals
4.1 Line Plot
When the Line Plot button (left panel) is clicked, the right panel displays 3 checkboxes for selecting 1D function curves:
Radial Wave Function : Shows the variation of the atomic orbital's radial wave function with radius.
Square of Radial Function : Displays the squared radial wave function, reflecting radial probability density.
Radial Distribution Function : Illustrates the probability of finding an electron near a spherical surface of radius.
 
Operation:
Select at least one option by checking the corresponding box(es). Click the Confirm button.
The program will call the main_R module to generate and display the selected line plots. In the pop-up interface: On the right panel, enter the principal quantum number n and azimuthal quantum number l. Click the Calculate button. The corresponding image will be displayed on the left panel.
 
4.2 2D Plot
When 2D Plot button (left panel) is clicked, the right panel displays 5 radio buttons (only one option can be selected), corresponding to five types of 2D function distribution plots:
Polar plot of Y : Displays the angular distribution of spherical harmonics (Ylm) in polar oordinates.
Polar plot of Y Squared : Shows the squared spherical harmonics in polar coordinates, reflecting angular probability density.
Contour of Ψ : Renders contour lines of the wave function on a 2D plane.
Contours of Ψ : Displays multiple contour sets of the wave function for detailed spatial analysis.
Contour of Ψ Squared : Illustrates contour lines of the squared wave function, representing probability density.
Operation:
Select one option and click the Confirm button.
The program calls the corresponding module (e.g., main_Y2D, main_squY2D, main_Psi2D) to generate and display the 2D plot. In the pop-up interface: On the right panel, enter the quantum numbers. Select different projection planes in the select plot option. Click the Calculate button. The corresponding image will be displayed on the left panel.

 
 
 
4.3 3D Plot
When 3D Plot button (left panel) is clicked, the right panel displays 6 radio buttons (only one option can be selected), corresponding to five types of 3D function distribution plots:
Polar plot of Y : Displays the angular distribution of spherical harmonics in 3D space.
Polar plot of Y Squared : Shows the squared spherical harmonics in 3D space, reflecting angular probability density1.
Isosurface of Ψ : Renders an isosurface where the wave function takes a specific constant value.
Isosurfaces of Ψ : Displays multiple isosurfaces of for comprehensive spatial analysis.
Electron Cloud : Simulates the probability distribution of electrons in 3D space based on electron density.
Superposition of 2 Ψ : Visualizes the spatial distribution resulting from the superposition of two wave functions.
 
Operation:
Select one option and click the Confirm button.
The program calls the corresponding module (e.g., main_Y3D, main_squY3D, main_isoPsi, main_cloudPsi) to generate and display the 3D plot. In the pop-up interface: On the right panel, enter the quantum numbers. The corresponding image will be displayed on the left panel.
 
 
 
 
