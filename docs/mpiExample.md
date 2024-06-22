# MPI Example

![MPI example Image](https://topology-tool-kit.github.io/img/gallery/mpiExample.png)

This example demonstrates the use of TTK algorithms in parallel. The original data set is small and resampled to $256^3$ but this dimension can be changed to fit any machine resources. 

For more information on how to run a pipeline in parallel in ParaView, please refer to the following ParaView documentation for [compilation]((https://kitware.github.io/paraview-docs/latest/cxx/Offscreen.html)) and for [use](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html) .

Please note both ParaView and TTK need to be compiled with MPI to allow for parallel execution in a distributed context. 

## Pipeline description

The produced visualization captures the covalent and hydrogen bonds within the molecule complex as well as shows where the electronic density experiences rapid changes, indicating transition points occurring within the bond.

First, the magnitude of the scalar field is computed and the data set is resampled to $256^3$. This dimension can be changed (see the commands below).

Then, both the scalar field and its magnitude are smoothed via [ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html) and normalized via [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html).

Next, the critical points of the scalar field are computed via [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) and used as seeds of the [IntegralLines](https://topology-tool-kit.github.io/doc/html/classttkIntegralLines.html).

Next, the geometry of the integral lines is smoothed using the [GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html). 

Finally, the critical points of the magnitude are computed on the smoothed geometry of the integral lines.

## ParaView
To reproduce the above screenshot on 4 processes and 2 threads, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:

``` bash
OMP_NUM_THREADS=2 mpirun -n 4 pvserver 
``` 
Then enter the following command:
``` bash
paraview 
```
Now, follow the procedure described in paragraphs $7.2.2$ and $7.2.3$ of the following [ParaView documentation](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html#configuring-a-server-connection) to connect your ParaView server to your client. Once that is done, you can open the state file `state/mpiExample.pvsm` in the ParaView GUI through `File` > `Load State`. 


## Python code

``` python  linenums="1"
--8<-- "python/mpiExample.py"
```

To run the above Python script using 2 threads and 4 processes, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
OMP_NUM_THREADS=2 mpirun -n 4 pvbatch mpiExample.py 
```
Regarding performance, the optimal configuration depends on the architecture and on the OpenMP and OpenMPI versions. For example, to perform on 24-core nodes (without SMT -- simultaneous multithreading) using 64 nodes:

``` bash
OMPI_MPI_THREAD_LEVEL=1 OMP_PLACES=cores OMP_PROC_BIND=close OMP_NUM_THREADS=24 mpirun --bind-to none --map-by node --mca btl_openib_btls_per_lid 8 -n 64 pvbatch pipeline.py
```

By default, the dataset is resampled to $256^3$. To resample to a higher dimension, for example $2048^3$, enter the following command:

```bash
OMP_NUM_THREADS=2 mpirun -n 4 pvbatch pipeline.py 2048
```
Be aware that this will require a lot of memory to execute and will most likely not be possible on a regular laptop.



## Inputs
- [at.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/at.vti): A molecular dataset: a three-dimensional regular grid with one scalar field, the electronic density in the Adenine Thymine complex.

## Outputs
- `integralLines.pvtu`: the geometry of the smoothed integral lines capturing the covalent and hydrogen bonds of the molecule, as extracted by the analysis pipeline.
- `criticalPoints.pvtu`: the critical points computed on the geometry of the integral lines, showing the rapid changes in the bonds.

## C++/Python API

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)

[IntegralLines](https://topology-tool-kit.github.io/doc/html/classttkIntegralLines.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

