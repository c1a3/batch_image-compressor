from PIL import Image as im

def compress_image(file_path, output_directory, compression_quality=75):
    
    try:
        with im.open(file_path) as image:
            original_size = file_path.stat().st_size  
            output_path = output_directory / file_path.name
            image.save(output_path, optimize=True, quality=compression_quality)  # custom qualitty
            
            compressed_size = output_path.stat().st_size  # size in bytes
            
            compression_percentage = (1 - compressed_size / original_size) * 100
            
            print(f"Compressed {file_path} to {output_path}. Compression: {compression_percentage:.2f}%")
    except Exception as e:
        print(f"Error compressing {file_path}: {e}")

//
