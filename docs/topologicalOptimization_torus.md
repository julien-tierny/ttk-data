# Topological Optimization Torus

![Topological Optimization Torus example Image]()

## Pipeline description
This example simplifies a handle on a surface corresponding to a torus.

This example first loads the surface.
It then computes a signed distance field to create a scalar field defined on a regular grid using [SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html).
The persistence diagram is computed using [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) and then thresholded to create a target diagram where only the persistence pair with infinite persistence is kept.
Finally, using the numerical optimization backend of [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html), it optimizes the scalar field to remove the handle.

The python script computes the topological optimization and saves the optimized scalar fields with the cutting and the filling strategies.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topologicalOptimization_torus.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/topologicalOptimization_torus.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/topologicalOptimization_torus.py
```

## Inputs
- [torus.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/torus.vtu): A surface representing a torus.

## Outputs
-  `topoOpt_torus_fill.vti`: the optimized dataset with the fill strategy.
-  `topoOpt_torus_cut.vti`: the optimized dataset with the cut strategy.

## C++/Python API

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

