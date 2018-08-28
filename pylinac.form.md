<!-- markdownlint-disable MD033 -->

# CatPhan analysis with Python, PyLinac, and ScriptedForms

This is a ScriptedForm. It allows you to easily make printable user interfaces that can be hosted on your intranet. ScriptedForms are powered by Python and all the goodies that come with that.

The Python goodie we will be focusing on in this form is PyLinac.

## Select a Dicom zip file

To begin, select one of the zip files within the `data` directory. By default there is only one zip file in there containing a Cone Beam CT of a CatPhan. You can of course reuse this form and drop other files within the data directory as you please.

<variable-dropdown items="zip_filepaths" label="Select the conebeam zip file">
  selected_zip_file
</variable-dropdown>


<section-button conditional="selected_zip_file" value="Load DICOM zip file">

```python
display(Markdown('Loading...'))
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    cbct = CatPhan504.from_zip(selected_zip_file)

number_of_slices = len(cbct.dicom_stack)
display(Markdown('Successfully loaded `{}`'.format(selected_zip_file)))
```

</section-button>

## Peruse Slices

<section-live>

<variable-slider min="1" max="number_of_slices" label="Select a slice">
  chosen_slice
</variable-slider>

```python
plt.imshow(cbct.dicom_stack[chosen_slice - 1]);
```

</section-live>








<section-start onLoad>

```python
from glob import glob
import warnings

import matplotlib.pyplot as plt

from IPython.display import display, Markdown

import pydicom
from pylinac import CatPhan504

zip_search_string = 'data/*.zip'
selected_zip_file = None
number_of_slices = 0
chosen_slice = 0
```

</section-start>

<section-filechange onLoad paths="[zip_search_string]">

```python
zip_filepaths = glob(zip_search_string)
if len(zip_filepaths) == 1:
    selected_zip_file = zip_filepaths[0]
```

</section-filechange>