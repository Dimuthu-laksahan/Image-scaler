from realesrgan import RealESRGAN
from PIL import Image
import torch
import os
import sys
import argparse

def check_dependencies():
    """Check if all required dependencies are available"""
    try:
        import cv2
        import numpy as np
        print("✓ All dependencies are available")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def upscale_image(input_path, output_path, model_path=None, scale=4):
    """
    Upscale an image using Real-ESRGAN
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save upscaled image
        model_path (str): Path to model weights (optional)
        scale (int): Upscaling factor (2, 4, or 8)
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image not found: {input_path}")
        
        # Check CUDA availability
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {device}")
        
        # Initialize model
        print(f"Loading Real-ESRGAN model with {scale}x upscaling...")
        model = RealESRGAN(device, scale=scale)
        
        # Load weights
        if model_path and os.path.exists(model_path):
            model.load_weights(model_path)
            print(f"✓ Loaded custom weights from: {model_path}")
        else:
            # Try to load default weights
            default_weights = {
                2: 'weights/RealESRGAN_x2plus.pth',
                4: 'weights/RealESRGAN_x4plus.pth',
                8: 'weights/RealESRGAN_x8.pth'
            }
            
            weight_path = default_weights.get(scale)
            if weight_path and os.path.exists(weight_path):
                model.load_weights(weight_path)
                print(f"✓ Loaded default weights for {scale}x upscaling")
            else:
                print(f"⚠️  Warning: No weights found. Model will use random initialization.")
                print(f"   Please download weights from: https://github.com/xinntao/Real-ESRGAN/releases")
        
        # Open and validate image
        print(f"Opening image: {input_path}")
        img = Image.open(input_path).convert('RGB')
        print(f"Image size: {img.size}")
        
        # Check image size limitations
        max_pixels = 4000 * 4000  # Adjust based on your GPU memory
        if img.size[0] * img.size[1] > max_pixels:
            print(f"⚠️  Warning: Large image detected. Consider resizing input image.")
        
        # Perform upscaling
        print("Starting upscaling process...")
        with torch.no_grad():
            sr_image = model.predict(img)
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save output
        sr_image.save(output_path, quality=95)
        print(f"✓ Upscaled image saved to: {output_path}")
        print(f"Output size: {sr_image.size}")
        
        return True
        
    except FileNotFoundError as e:
        print(f"❌ File error: {e}")
        return False
    except torch.cuda.OutOfMemoryError:
        print("❌ CUDA out of memory. Try using CPU or reduce image size.")
        return False
    except Exception as e:
        print(f"❌ Error during upscaling: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Image Super-Resolution using Real-ESRGAN')
    parser.add_argument('input', help='Input image path')
    parser.add_argument('-o', '--output', help='Output image path', default='output_upscaled.png')
    parser.add_argument('-s', '--scale', type=int, choices=[2, 4, 8], default=4, 
                       help='Upscaling factor (default: 4)')
    parser.add_argument('-w', '--weights', help='Path to model weights')
    parser.add_argument('--check', action='store_true', help='Check dependencies only')
    
    args = parser.parse_args()
    
    if args.check:
        check_dependencies()
        return
    
    print("Real-ESRGAN Image Upscaler")
    print("=" * 30)
    
    # Check dependencies first
    if not check_dependencies():
        print("Please install missing dependencies using: pip install -r requirements.txt")
        return
    
    # Perform upscaling
    success = upscale_image(args.input, args.output, args.weights, args.scale)
    
    if success:
        print("\n✓ Image upscaling completed successfully!")
    else:
        print("\n❌ Image upscaling failed. Please check the error messages above.")

if __name__ == "__main__":
    # Default behavior when run without arguments
    if len(sys.argv) == 1:
        print("Real-ESRGAN Image Upscaler")
        print("=" * 30)
        print("Usage examples:")
        print("  python img-scaler.py input.jpg")
        print("  python img-scaler.py input.jpg -o output.png -s 4")
        print("  python img-scaler.py --check  # Check dependencies")
        print("\nFor help: python img-scaler.py -h")
        
        # Try default upscaling if input.jpg exists
        if os.path.exists('input.jpg'):
            print("\nFound 'input.jpg', running default upscaling...")
            upscale_image('input.jpg', 'output_upscaled.png')
        else:
            print("\nNo input.jpg found. Please provide an input image.")
    else:
        main()
