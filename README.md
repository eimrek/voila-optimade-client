# OPTiMaDe client for AiiDA Lab

Query for and import structures from [OPTiMaDe](https://www.optimade.org) providers (COD, Materials Cloud, NoMaD, Materials Project, OQMD, and more ...)  
Note, this application handles the structures by converting them to ASE `Atoms` or AiiDA `StructureData` objects.

Current OPTiMaDe API version: `0.10.1`

## Installation

This Jupyter-based app is intended to run in [AiiDA Lab](https://aiidalab.materialscloud.org) as well as inside a [Quantum Mobile](https://materialscloud.org/work/quantum-mobile) Virtual Machine.

Use the App Store in the [Home App](https://github.com/aiidalab/aiidalab-home) to install it.

## Usage

### Default

To use the OPTiMaDe structure importer in your own AiiDA Lab app write the following:

```python
from aiidalab_optimade import OptimadeQueryWidget
from aiidalab_widgets_base.viewers import StructureDataViewer
from ipywidgets import dlink

structure_query = OptimadeQueryWidget()
structure_viewer = StructureDataViewer()

_ = dlink((structure_query, 'structure'), (structure_viewer, 'structure'))  # Save to `_` in order to suppress output in App Mode

display(structure_query)
display(structure_viewer)
```

This will immediately display a query widget with a dropdown of current structure databases that implements the OPTiMaDe API.

Then you can filter to find a family of structures according to elements, number of elements, chemical formula, and more.
See the [OPTiMaDe API specification document](https://github.com/Materials-Consortia/OPTiMaDe/blob/master/optimade.rst) for the full list and their description.

In order to get tabs delving deeper into the details of a particular structure, you can also import and display `OptimadeResultsWidget`.
The link for this should then look like: `_ = dlink((structure_query, 'structure'), (structure_output, 'entity'))`, given that you initiate `OptimadeResultsWidget` in the variable `structure_output`.

See the notebook [`OPTiMaDe general.ipynb`](OPTiMaDe general.ipynb) for an example of how to set up a general purpose OPTiMADe importer.

### Embedded

The query widget may also be embedded into another app.  
For this a more "minimalistic" version of the widget can be initiated by passing `embedded=True` upon initiating the widget, i.e., `structure_query = OptimadeQueryWidget(embedded=True)`.

Everything else works the same - so you would still have to link up the query widget to the rest of your app.

## License

MIT. The terms of the license can be found in the LICENSE file.

## Contact

aiidalab@materialscloud.org
casper.andersen@epfl.ch
