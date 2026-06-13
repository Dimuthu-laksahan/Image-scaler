<<<<<<< HEAD
# Real-ESRGAN Image Upscaler

A Python application for high-quality image super-resolution using Real-ESRGAN AI models.

## Features

- **Multiple Upscaling Factors**: Support for 2x, 4x, and 8x image upscaling
- **GPU Acceleration**: CUDA support with automatic CPU fallback
- **User-Friendly Interface**: Command-line interface with helpful error messages
- **Robust Error Handling**: Comprehensive validation and error recovery
- **Flexible Input**: Support for various image formats (JPEG, PNG, etc.)

## Installation

1. **Clone or download this project**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download model weights** (required for proper functionality):
   
   Create a `weights` directory and download the appropriate model weights:
   
   ```bash
   mkdir weights
   ```
   
   Download from [Real-ESRGAN releases](https://github.com/xinntao/Real-ESRGAN/releases):
   - For 4x upscaling: `RealESRGAN_x4plus.pth`
   - For 2x upscaling: `RealESRGAN_x2plus.pth`
   - For 8x upscaling: `RealESRGAN_x8.pth`

## Usage

### Basic Usage

```bash
# Upscale input.jpg with default settings (4x)
python img-scaler.py input.jpg

# Specify output file and scale factor
python img-scaler.py input.jpg -o output.png -s 4

# Use custom model weights
python img-scaler.py input.jpg -w weights/RealESRGAN_x4plus.pth
```

### Command Line Options

```bash
python img-scaler.py [input_image] [options]

Options:
  -o, --output    Output image path (default: output_upscaled.png)
  -s, --scale     Upscaling factor: 2, 4, or 8 (default: 4)
  -w, --weights   Path to custom model weights
  --check         Check if all dependencies are installed
  -h, --help      Show help message
```

### Examples

```bash
# Check if dependencies are properly installed
python img-scaler.py --check

# Upscale with 2x factor
python img-scaler.py photo.jpg -o photo_2x.png -s 2

# Process multiple images (use shell scripting)
for img in *.jpg; do python img-scaler.py "$img" -o "upscaled_$img"; done
```

## Requirements

- Python 3.7+
- PyTorch (with CUDA support recommended)
- Real-ESRGAN
- Pillow (PIL)
- OpenCV
- NumPy

## System Requirements

- **GPU**: NVIDIA GPU with CUDA support (recommended for faster processing)
- **RAM**: 8GB+ recommended for processing large images
- **Storage**: Additional space for model weights (~100MB per model)

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

2. **CUDA out of memory**: Reduce image size or use CPU mode

3. **Model weights not found**: Download the appropriate weights from the Real-ESRGAN repository

4. **Slow processing**: Ensure CUDA is properly installed and GPU is being used

### Performance Tips

- Use CUDA-enabled GPU for faster processing
- For very large images, consider resizing input before upscaling
- Close other GPU-intensive applications while processing
- Use appropriate model weights for your desired upscaling factor

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Add tests if applicable
5. Submit a pull request

## License

This project uses Real-ESRGAN which is licensed under the BSD 3-Clause License.

## Acknowledgments

- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) by Xintao Wang et al.
- [BasicSR](https://github.com/XPixelGroup/BasicSR) library
- PyTorch team for the deep learning framework
=======
# Image-scaler
>>>>>>> 6d70f16d7512cd629522abec92842a55b025bd50
