# People250 Dataset

The **People250** dataset consists of 250 images containing people, along with corresponding prompts and masks.

---

## 📂 Dataset Structure

```plaintext
People250/
├── original/                   # Original 250 images containing people
├── prompts/                    # Prompts used for generation/inpainting (text format)
├── masks/                      # Masks used during inpainting experiments
├── clean_inpainted/            # Inpainted results without adversarial protection
│   ├── baseline/               # Baseline results with default diffusion model
│   └── <other_experiments>     # Future inpainting results under various settings
├── adversarial/                # Adversarial protection experiments
│   ├── <experiment_name>/      # E.g., "DiffJPEG experiments", "Original DDD"
│   │   ├── protected/          # Watermarked/protected images
│   │   └── generated/          # Output after running diffusion models
├── metadata/                   # Details of experiment configurations
│   └── <experiment_name>.md    # Experiment-specific parameters (seed, model settings, etc.)
└── README.md                   # This file
```

## 🔍 Folder Details

> 📝 Filenames
>
> Filenames of protected and generated images should be identical to the corresponding original image, i.e., `1234.png`.

`original/`

* Contains the 250 original images featuring people.
* These are untouched and serve as the baseline for all experiments.

`prompts/`

* Text files containing the prompts used for inpainting.
* File naming convention matches original/ for easy cross-referencing.

`masks/`

* Contains binary masks used during inpainting.
* Masks correspond to regions in `original/` images that were targeted for inpainting.

`clean_inpainted/`

* Contains inpainting results without adversarial protection.
* Useful as a baseline for evaluating the effectiveness of adversarial methods.

**Example Subfolders:**

* `/baseline/`: Inpainting using standard diffusion models.
* `/<experiment_name>/`: Future experiments with varied parameters (e.g., different inpainting strengths and guidance scales).

`adversarial/`

* Contains adversarial protection experiments, including watermarked images and the resulting generated images after running stable diffusion inpainting.

**Example Subfolders:**

```plaintext
adversarial/
├── optimised_ddd/
│   ├── protected/    # Watermarked images from Jakub's optimised DDD
│   └── generated/    # Diffusion model outputs after protection
├── photoguard/
│   ├── protected/    # Photoguard-protected images
│   └── generated/    # Corresponding generated results
```

`metadata/`

* Stores experiment settings.
* Ensures reproducibility by recording parameters like:
    * Diffusion model
    * Diffusion model settings
    * Random seeds
    * Adversarial settings

An example is stored as `template.md`.

## 🏃 Usage Instructions

### 🔄 Cloning the Repository
```bash
git clone https://github.com/Alf4ed/fourth-year-project-dataset.git
```

## 🧪 Running Experiments
To ensure consistency with recorded experiments:

1. Check the corresponding `metadata/` file for settings.
2. Use `original/`, `prompts/`, and `masks/` as inputs.
3. Output results should follow the `adversarial/<experiment_name>/` or `clean_inpainted/<experiment_name>/` structure.

## 🤝 Related Repository
This dataset complements the main project repository:

👉 Main Project: [Diffusion Based Adversarial Perturbations for Disrupting Deepfake Generation](https://github.com/JakubCzarlinski/fourth-year-project)
