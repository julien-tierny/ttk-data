# Topological Optimization DarkySky

![Topological Optimization DarkySky example Image]()

## Pipeline description
This example simplifies all the persistence pairs below 25% of the maximum persistence of the density of dark matter in an astrophysics simulation.

This example first loads the point cloud then applies a gaussian resampling to create a scalar field defined on a regular grid.
Then the scalar field is smoothed with [ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html) (with 5 iterations) and normalized with [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html).
The persistence diagram is computed using [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) and then thresholded to create a target diagram where the persistence pairs having persistence below 25% of the maximum persistence are removed.
Finally, using the numerical optimization backend of [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html), it optimizes the scalar field to remove the most possible the pairs not in the target diagram.

The python script computes the topological optimization and saves the optimized scalar field.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topologicalOptimization_darkySky.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/topologicalOptimization_darkySky.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/topologicalOptimization_darkySky.py
```

## Inputs
- [ds14_scivis_0128_e4_dt04_1.0000.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/ds14_scivis_0128_e4_dt04_1.0000.vtp): A point cloud dataset representing a simulation of the density of dark matter in the universe.

## Outputs
-  `darkSky_optimized.vti`: the optimized dataset.

## C++/Python API

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
