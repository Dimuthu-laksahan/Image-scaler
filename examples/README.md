# Example Usage

This directory contains example images and usage scenarios for the Real-ESRGAN image upscaler.

## Sample Images

Place your test images here to experiment with the upscaler:

- `input.jpg` - Sample input image for testing
- `output_upscaled.png` - Example output after 4x upscaling
- `comparison/` - Before/after comparison images

## Usage Examples

### Basic Upscaling
```bash
# From the project root directory
python img-scaler.py examples/input.jpg -o examples/output_4x.png
```

### Different Scale Factors
```bash
python img-scaler.py examples/input.jpg -o examples/output_2x.png -s 2
python img-scaler.py examples/input.jpg -o examples/output_8x.png -s 8
```

## Tips for Best Results

1. **Input Quality**: Higher quality input images generally produce better results
2. **File Formats**: PNG format preserves quality better than JPEG for outputs
3. **Image Size**: Very small images may not benefit significantly from upscaling
4. **Content Type**: Real-ESRGAN works particularly well on photos and natural images
