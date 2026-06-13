<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Real-ESRGAN Image Upscaler Project

This is a Python project for image super-resolution using Real-ESRGAN. The project provides:

- High-quality image upscaling using state-of-the-art AI models
- Support for 2x, 4x, and 8x upscaling factors
- GPU acceleration with CUDA support
- Robust error handling and user-friendly interface
- Command-line interface with various options

## Development Guidelines

When working with this project:

1. **Dependencies**: Always ensure PyTorch, Real-ESRGAN, and OpenCV are properly installed
2. **GPU Support**: Code should gracefully fallback to CPU if CUDA is not available
3. **Error Handling**: Include comprehensive error handling for file operations and memory issues
4. **Performance**: Consider memory limitations when processing large images
5. **Model Weights**: Provide clear instructions for downloading required model weights

## Key Components

- `img-scaler.py`: Main upscaling script with CLI interface
- `requirements.txt`: Python dependencies
- `weights/`: Directory for storing model weights (to be created)
- `examples/`: Sample input/output images (to be created)

## Best Practices

- Use type hints for function parameters
- Include docstrings for all functions
- Implement proper logging for debugging
- Add progress indicators for long-running operations
- Validate input parameters and file formats
