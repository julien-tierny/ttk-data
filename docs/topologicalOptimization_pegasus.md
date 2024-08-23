# Topological Optimization Pegasus

![Topological Optimization Pegasus example Image]()

## Pipeline description
This example simplifies a defect handle on a surface corresponding to a pegasus.

This example first loads the surface and clip it to extract the defect handle.
It then computes a signed distance field to create a scalar field defined on a regular grid using [SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html).
The persistence diagram is computed using [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) and then thresholded to create a target diagram where the persistence pair corresponding to the defect handle is removed.
Finally, using the numerical optimization backend of [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html), it optimizes the scalar field to remove the defect handle.

The python script computes the topological optimization and saves the optimized scalar fields with the cutting and the filling strategies.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topologicalOptimization_pegasus.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/topologicalOptimization_pegasus.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/topologicalOptimization_pegasus.py
```

## Inputs
- [pegasus.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/pegasus.vtu): A surface representing a pegasus.

## Outputs
-  `topoOpt_pegasus_fill.vti`: the optimized dataset with the fill strategy.
-  `topoOpt_pegasus_cut.vti`: the optimized dataset with the cut strategy.

## C++/Python API

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
