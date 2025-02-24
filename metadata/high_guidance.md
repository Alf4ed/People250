# Experiment Name: clean_inpainted/high_guidance

## Overview
Images inpainted using higher strength and guidance scale to improve prompt alignment.

- **Date Conducted**: 24-02-2025

## Experiment Parameters

- **Input Images**: original
- **Base Model**: stabilityai/stable-diffusion-2-inpainting
- **Protection Method**: None
- **Resolution**: 512x512
- **Seed**: 1007
- **Inpainting Strength**: 1.0
- **Inpainting Guidance Scale**: 18.0

## Additional Notes

This experiment increases the inpainting strength to 1.0 to rely entirely on model-generated content within masked areas, reducing influence from the original image. The guidance scale was raised to 18.0 to push the model toward better alignment with the input prompts.

Preliminary observations show enhanced coherence with prompt descriptions. Further tuning may be required to balance prompt alignment and naturalistic output.