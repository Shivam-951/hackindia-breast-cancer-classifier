# Publish this project under your own GitHub account

1. Create a **public** repository named `hackindia-breast-cancer-classifier` under `Shivam-951`.
2. Do not add a README or license from GitHub if you are uploading these files as-is (this folder already contains a README).
3. In PowerShell, open this project folder and run:

```powershell
git init
git add .
git commit -m "Add scikit-learn breast cancer classification project"
git branch -M main
git remote add origin https://github.com/Shivam-951/hackindia-breast-cancer-classifier.git
git push -u origin main
```

4. Open the repository on GitHub and confirm that it is **Public** and the notebook, README, `train.py`, and `requirements.txt` are visible.
5. Run `python train.py` locally before submitting and keep the actual terminal output for your submission.
6. Submit the public repository URL in HackIndia.

GitHub commits must be made/authored by your `@Shivam-951` account. This package does not publish or commit anything to GitHub for you.
