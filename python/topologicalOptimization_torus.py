#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
torusvtu = XMLUnstructuredGridReader(FileName=["torus.vtu"])
torusvtu.CellArrayStatus = ["GroupIds"]
torusvtu.TimeArray = "None"

# create a new 'TTK SignedDistanceField'
tTKSignedDistanceField1 = TTKSignedDistanceField(Input=torusvtu)
tTKSignedDistanceField1.SamplingDimensions = [64, 64, 64]
tTKSignedDistanceField1.FastMarchingOrder = "1"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKSignedDistanceField1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "signedDistanceField"]
tTKPersistenceDiagram1.InputOffsetField = ["POINTS", "edgeCrossing"]
tTKPersistenceDiagram1.EmbedinDomain = 1

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ["CELLS", "IsFinite"]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=tTKSignedDistanceField1, Constraints=threshold2
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "signedDistanceField"]
tTKTopologicalSimplification1.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification1.InputOffsetField = ["POINTS", "edgeCrossing"]
tTKTopologicalSimplification1.VertexIdentifierField = ["POINTS", "CriticalType"]
tTKTopologicalSimplification1.StoppingConditionCoefficient = 0.001
tTKTopologicalSimplification1.MaximumIterationNumber = 2000
tTKTopologicalSimplification1.CancellationPrimitive = "Cut-only"
tTKTopologicalSimplification1.GradientStepSize = 0.9

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=tTKTopologicalSimplification1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "signedDistanceField"]
tTKScalarFieldSmoother1.MaskField = ["POINTS", "edgeCrossing"]

# create a new 'Contour'
contour2 = Contour(Input=tTKScalarFieldSmoother1)
contour2.ContourBy = ["POINTS", "signedDistanceField"]
contour2.Isosurfaces = [0.0]
contour2.PointMergeMethod = "Uniform Binning"

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(
    Domain=tTKSignedDistanceField1, Constraints=threshold2
)
tTKTopologicalSimplification2.ScalarField = ["POINTS", "signedDistanceField"]
tTKTopologicalSimplification2.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification2.InputOffsetField = ["POINTS", "edgeCrossing"]
tTKTopologicalSimplification2.VertexIdentifierField = ["POINTS", "CriticalType"]
tTKTopologicalSimplification2.StoppingConditionCoefficient = 0.001
tTKTopologicalSimplification2.MaximumIterationNumber = 2000
tTKTopologicalSimplification2.CancellationPrimitive = "Fill-only"
tTKTopologicalSimplification2.GradientStepSize = 0.9

# create a new 'Contour'
contour3 = Contour(Input=tTKTopologicalSimplification2)
contour3.ContourBy = ["POINTS", "signedDistanceField"]
contour3.Isosurfaces = [0.0]
contour3.PointMergeMethod = "Uniform Binning"

SaveData("topoOpt_torus_cut.vtu", contour2)
SaveData("topoOpt_torus_fill.vtu", contour3)
