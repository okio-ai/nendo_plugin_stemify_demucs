# Advanced Usage

### Changing the default model

Per default the `htdemucs_6s` model is used
and 6 different stem_types will be extracted: `vocals`, `drums`, `bass`, `other`, `piano`, `guitar`.

To change the model, simply pass the `model` parameter to the plugin:

```python
stems = nd.plugins.stemify_demucs(
    track=track,
    model="mdx_extra"
)
```
!!! warning 
    Only `htdemucs_6s` supports all 6 stem_types. 
    For other models refer to the official demucs [documentation](https://github.com/facebookresearch/demucs).


Since we build on top of `demucs`, all models from `demucs` are available.

| Model Name         | Description                                                 | Notes                                                                          |
|--------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------|
| htdemucs           | First version of Hybrid Transformer Demucs.                 | Trained on MusDB + 800 songs. Default model.                                   |
| htdemucs_ft        | Fine-tuned version of htdemucs.                             | Separation takes 4x more time, might be better. Same training set as htdemucs. |
| htdemucs_6s        | 6 sources version of htdemucs, with piano and guitar added. | Piano source not performing well currently.                                    |
| hdemucs_mmi        | Hybrid Demucs v3.                                           | Retrained on MusDB + 800 songs.                                                |
| mdx                | Trained only on MusDB HQ.                                   | Winning model on track A at the MDX challenge.                                 |
| mdx_extra          | Trained with extra data.                                    | Includes MusDB test set, 2nd on track B of MDX challenge.                      |
| mdx_q, mdx_extra_q | Quantized versions of mdx and mdx_extra.                    | Smaller download and storage, slightly worse quality.                          |
| SIG                | Single model from the model zoo.                            | -                                                                              |

For more information go to [their github page](https://github.com/facebookresearch/demucs)

## Changing the `stem_types` parameter

This parameter allows finer grained control on the resulting stems you want to extract.
Per default the following stem_types are available: `vocals`, `drums`, `bass`, `other`, `piano`, `guitar`.
However if for example you only want to extract the vocals and the background, you can do so by passing the following parameter:

```python
stems = nd.plugins.stemify_demucs(
    track=track,
    stem_types=["vocals", "no_vocals"],
    model="mdx_extra"
)
```

Of course this works with all stem types, so to extract the drums from a track you can do:

```python
stems = nd.plugins.stemify_demucs(
    track=track,
    stem_types=["drums", "no_drums"],
    model="mdx_extra"
)
```

