# Experiment Name: clean_inpainted/baseline

## Overview
Images inpainted using default settings

- **Date Conducted**: 24-02-2025

## Experiment Parameters

- **Input Images**: original
- **Base Model**: stabilityai/stable-diffusion-2-inpainting
- **Protection Method**: None
- **Resolution**: 512x512
- **Seed**: 1007
- **Inpainting Strength**: 0.8
- **Inpainting Guidance Scale**: 7.5

## Additional Notes
Baseline results using default inpainting parameters as used by DDD and Photoguard.

Outputs indicate that default *strength* and *guidance_scale* may not be suitable. Generated results do not closely correlate with the prompts.

Try generating new images with *stength* closer to 1 and a larger *guidance_scale* value.