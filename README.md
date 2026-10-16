# Breast Cancer Classification with Scikit-learn

A beginner-friendly machine-learning project that trains and evaluates a classification model to predict whether a breast tumour sample is **benign** or **malignant** using the Wisconsin Diagnostic Breast Cancer dataset.

## Dataset source
- Dataset: Wisconsin Diagnostic Breast Cancer (WDBC)
- Original source: UCI Machine Learning Repository — https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- Loaded through scikit-learn's built-in `load_breast_cancer()` dataset loader. The dataset is bundled with scikit-learn, so no separate dataset download is needed.

This is an educational demonstration, not a medical diagnostic tool.

## Model and method
- Model: `RandomForestClassifier`
- Split: 80% training / 20% testing
- Reproducibility: `random_state=42`
- Evaluation: accuracy, precision, recall, F1-score, confusion matrix, and classification report
- Preprocessing: stratified split to preserve class proportions

## Project files
- `breast_cancer_classification.ipynb` — end-to-end notebook with dataset inspection, split, training, and evaluation
- `train.py` — runnable script that trains and evaluates the model
- `requirements.txt` — Python dependencies

## Run locally
Python 3.10+ recommended.

```bash
git clone https://github.com/Shivam-951/hackindia-breast-cancer-classifier.git
cd hackindia-breast-cancer-classifier
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python train.py
```

To run the notebook:

```bash
jupyter notebook breast_cancer_classification.ipynb
```

## Expected output
The script prints the dataset dimensions, train/test sizes, accuracy, precision, recall, F1-score, confusion matrix, and classification report. Exact metrics can vary slightly with library versions, but the fixed random seed makes the split and model reproducible for the same environment.

## Important limitation
The model is trained on a small, curated benchmark dataset and must not be used for clinical decisions. Model performance on this dataset does not imply real-world medical reliability.
