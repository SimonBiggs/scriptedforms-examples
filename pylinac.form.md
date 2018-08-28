<!-- markdownlint-disable MD033 -->

# Conebeam

<section-start onLoad>

```python
from glob import glob
from IPython.display import display, Markdown
from pylinac import CatPhan504

zip_search_string = 'data/*.zip'
selected_zip_file = None
```

</section-start>

<section-filechange onLoad paths="[zip_search_string]">

```python
zip_filepaths = glob(zip_search_string)
if len(zip_filepaths) == 1:
    selected_zip_file = zip_filepaths[0]
    print('Only one file found, defaulting to selecting {}.'.format(selected_zip_file))
```

</section-filechange>

<variable-dropdown items="zip_filepaths" label="Select the conebeam zip file">
  selected_zip_file
<variable-dropdown>