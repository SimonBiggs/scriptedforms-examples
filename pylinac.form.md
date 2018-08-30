<!-- markdownlint-disable MD033 -->

# CatPhan analysis with Python, PyLinac, and ScriptedForms

This is a ScriptedForm. It allows you to easily make printable user interfaces that can be hosted on your intranet. ScriptedForms are powered by Python and all the goodies that come with that.

ScriptedForms are created with a plain text file. Any editing of that plain text
file will automatically update the displayed form. The plain text file for this
form is found at [this link](../../edit/pylinac.form.md). Open that link up in another tab, edit some of the file contents, save the result by pressing `Ctrl + S`, and then see the form update.

The Python goodie we will be focusing on in this form is PyLinac.

## Select a DICOM zip file

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
smallest_value = np.min([np.min(dcm.array) for dcm in cbct.dicom_stack])
largest_value = np.max([np.max(dcm.array) for dcm in cbct.dicom_stack])

display(Markdown('Successfully loaded `{}`'.format(selected_zip_file)))
```

</section-button>

## Peruse Slices

Once you have loaded up a DICOM data set you may peruse the slices using the following slider.

<section-live>

<variable-slider min="1" max="number_of_slices" label="Select a slice">
  chosen_slice
</variable-slider>

```python
current_image = cbct.dicom_stack[chosen_slice - 1]
plt.figure(figsize=(11,11))
plt.imshow(current_image, vmin=smallest_value, vmax=largest_value);
```

</section-live>

## Run Analysis

Once you have loaded up a DICOM data set you may analyse the CatPhan using PyLinac.

<section-button conditional="cbct is not None" value="Run Analysis">

```python
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    cbct.analyze()
    print(cbct.results())

    sub_images = ['hu', 'un', 'sp', 'lc', 'mtf', 'lin', 'prof']
    for sub_image in sub_images:
        cbct.plot_analyzed_subimage(sub_image)
```

</section-button>

## Conclusion

ScriptedForms can bring Python tools such as PyLinac into our every day job with little friction.

For documentation on ScriptedForms see <https://scriptedforms.com.au>. For documentation on PyLinac see <https://pylinac.readthedocs.io>.

To facilitate transfer of DICOM files from the Linac or CT to the ScriptedForms server I recommend using [Orthanc](https://www.orthanc-server.com/).

<section-start>

```python
from glob import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt

from IPython.display import display, Markdown

import pydicom
from pylinac import CatPhan504

zip_search_string = 'data/*.zip'
selected_zip_file = None
number_of_slices = 0
chosen_slice = 1
cbct = None
```

</section-start>

<section-filechange onLoad paths="[zip_search_string]">

```python
zip_filepaths = glob(zip_search_string)
if len(zip_filepaths) == 1:
    selected_zip_file = zip_filepaths[0]
```

</section-filechange>