"""Run the complete notebook in a fresh Jupyter kernel and save its outputs."""
from pathlib import Path
import asyncio
import json
import os
import platform
import tempfile
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]

def main():
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    path = ROOT / 'notebooks/01_study2_eda.ipynb'
    notebook = nbformat.read(path, as_version=4)
    runtime_root = ROOT / '.jupyter-runtime'
    runtime_root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=runtime_root) as runtime:
        keys = ['JUPYTER_RUNTIME_DIR', 'IPYTHONDIR', 'PYDEVD_DISABLE_FILE_VALIDATION', 'TEMP', 'TMP']
        old = {key: os.environ.get(key) for key in keys}
        previous_tempdir = tempfile.tempdir
        tempfile.tempdir = runtime
        os.environ.update(JUPYTER_RUNTIME_DIR=runtime, IPYTHONDIR=runtime,
                          PYDEVD_DISABLE_FILE_VALIDATION='1', TEMP=runtime, TMP=runtime)
        try:
            NotebookClient(notebook, timeout=120, startup_timeout=30, kernel_name='python3',
                           resources={'metadata': {'path': str(ROOT)}}).execute()
        finally:
            tempfile.tempdir = previous_tempdir
            for key, value in old.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
    code = [cell for cell in notebook.cells if cell.cell_type == 'code']
    assert all(cell.execution_count is not None for cell in code)
    assert not any(output.output_type == 'error' for cell in code for output in cell.outputs)
    images = sum('image/png' in output.get('data', {}) for cell in code for output in cell.outputs)
    assert images == 2
    notebook.metadata['execution_validation'] = {
        'engine': 'Fresh Jupyter kernel through nbclient', 'code_cells': len(code),
        'embedded_charts': images, 'separate_jupyter_kernel_transport_tested': True
    }
    nbformat.validate(notebook)
    nbformat.write(notebook, path)
    result = {'status': 'passed', 'code_cells': len(code), 'embedded_charts': images,
              'engine': 'Jupyter kernel / nbclient', 'python': platform.python_version()}
    (ROOT/'validation/jupyter_execution.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(f'PASS: {len(code)} notebook code cells executed in a fresh Jupyter kernel; {images} charts embedded.', flush=True)

if __name__ == '__main__':
    main()
