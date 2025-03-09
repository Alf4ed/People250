import os
from PIL import Image

def load_prompt(path):
    prompts = []
    with open(path, 'r') as f:
        for line in f:
            prompts.append(line)
    return prompts

prompt_files = [f for f in os.listdir('./prompts') if 'prompt' in f]

qualities = [80, 60, 50, 40, 20, 10]

for compression in qualities:
    output_path = f'diffjpeg_ddd/compressed/{str(compression)}'
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(f'./jpg/{output_path}', exist_ok=True)
    
    for prmt in prompt_files:
        testimg_filename = str(prmt[:-12])

        init_image = Image.open(f'./adversarial/diffjpeg_ddd/protected/{testimg_filename}_pert.png').convert('RGB').resize((512,512))

        init_image.save(f"./jpg/{output_path}/{testimg_filename}.jpg", format='JPEG', quality=compression)
        jpeg_image = Image.open(f"./jpg/{output_path}/{testimg_filename}.jpg").convert('RGB').resize((512,512))
        jpeg_image.save(f"{output_path}/{testimg_filename}.png", format='PNG')