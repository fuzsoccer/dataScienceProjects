# Obtain the two analysis inputs

The publication package does not bundle patient-level data. Download the OSF storage archive from [the source project](https://osf.io/mqbux/) and retain its source attribution and applicable terms.

From the extracted portfolio project folder:

```text
python src/prepare_data.py --archive /path/to/mqbux-osfstorage-archive.zip
```

On Windows, use a quoted local path, for example:

```text
python src/prepare_data.py --archive "C:\Users\YOUR_NAME\Downloads\mqbux-osfstorage-archive.zip"
```

This verifies the two CSVs against the release used for the analysis and places them under `data/raw/`. Different upstream file versions fail with an explanatory error instead of silently replacing the study inputs. The notebook reads these CSVs directly; it does not download or execute upstream code.

Required archive members:

- `Manuscript--Field trial data and code/data_deidentified/study_2_analysis_data_deid.csv`
- `Manuscript--Field trial data and code/data_deidentified/study_2_fulldata_deid.csv`

The private working package already includes the files. The dictionary and original R script are also available upstream; see `references/SOURCES.md`.
