# Nendo Plugin Stemify Demucs

<br>
<p align="left">
    <img src="https://okio.ai/docs/assets/nendo_core_logo.png" width="350" alt="Nendo Core">
</p>
<br>

![Documentation](https://img.shields.io/website/https/nendo.ai)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/okio_ai.svg?style=social&label=Follow%20%40okio_ai)](https://twitter.com/okio_ai) [![](https://dcbadge.vercel.app/api/server/XpkUsjwXTp?compact=true&style=flat)](https://discord.gg/XpkUsjwXTp)

---

Nendo Plugin for Music Source Separation (based on Meta [demucs](https://github.com/facebookresearch/demucs))

## Features

- Extract up to six different audio stems

## Installation

1. [Install Nendo](https://github.com/okio-ai/nendo#installation)
2. `pip install nendo-plugin-stemify-demucs`

## Usage

Take a look at a basic usage example below.
For more detailed information, please refer to the [documentation](https://okio.ai/docs/plugins).

For more advanced examples, check out the examples folder.
or try it in colab:

<a target="_blank" href="https://colab.research.google.com/drive/1rYBw5N0xzDf-NQJC1cQXqRBneBE8q4_z?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

```python
from nendo import Nendo, NendoConfig

nd = Nendo(config=NendoConfig(plugins=["nendo_plugin_stemify_demucs"]))

# load track
track = nd.library.add_track(file_path='/path/to/track.mp3')

# run stemification to get 6 stems
stems = nd.plugins.stemify_demucs(
    track=track,
    stem_types=["vocals", "drums", "bass", "other", "piano", "guitar"],
    model="htdemucs_6s"
)
vocals, drums = stems[0], stems[1]
drums.play()

# run stemification to get vocals and background
stems = nd.plugins.stemify_demucs(
    track=track,
    stem_types=["vocals", "no_vocals"],
    model="mdx_extra"
)

background = stems[1]
background.play()
```

## Contributing

Visit our docs to learn all about how to contribute to Nendo: [Contributing](https://okio.ai/docs/contributing/)


## License

Nendo: MIT License

Demucs: MIT License