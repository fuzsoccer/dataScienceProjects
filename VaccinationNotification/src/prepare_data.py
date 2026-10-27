"""Copy the two required CSV members from an OSF ZIP, checking their SHA-256.

Usage: python src/prepare_data.py --archive path/to/mqbux-osfstorage-archive.zip
Only these two members are read; no ZIP paths are extracted or executed.
"""
from argparse import ArgumentParser
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'study_2_analysis_data_deid.csv': '0329c09a27057eb5d234f3e248f8bdd9b176cd1d7008700809dc6b97fbcc412c',
    'study_2_fulldata_deid.csv': '55ae3d70ccc05e3126d57285d496da629400afbd4aea1d4c5163485480fd1277',
}
PREFIX = 'Manuscript--Field trial data and code/data_deidentified/'

def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--archive', required=True, type=Path)
    args = parser.parse_args()
    verified = {}
    with zipfile.ZipFile(args.archive) as archive:
        for name, digest in EXPECTED.items():
            content = archive.read(PREFIX + name)
            actual = hashlib.sha256(content).hexdigest()
            if actual != digest:
                raise ValueError(f'{name}: source version differs from the validated release. '
                                 'Review the upstream changes before updating the expected hash.')
            verified[name] = content
    destination = ROOT / 'data/raw'
    destination.mkdir(parents=True, exist_ok=True)
    for name, content in verified.items():
        path = destination / name
        if path.exists() and path.read_bytes() != content:
            raise FileExistsError(f'Refusing to replace different data: {path}')
        path.write_bytes(content)
        print(f'Verified {name}')

if __name__ == '__main__':
    main()
