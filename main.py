import pathlib
from compress import compress_image
def main():

    input_directory = pathlib.Path("images") 
    output_directory = pathlib.Path("compressed")

    # desired_compression_quality
    while True:
        try:
            desired_compression_quality = int(input("Enter desired compression quality (1-100): "))
            if 1 <= desired_compression_quality <= 100:
                break
            else:
                print("Please enter a value between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    output_directory.mkdir(parents=True, exist_ok=True) #If 'compressed' folder does not exists, will be created

    image_files = list(input_directory.rglob('*.*'))
    total_files = len(image_files)

    print(f"Total images to compress: {total_files}")

    for counter, file_path in enumerate(image_files):
        relative_dir = file_path.parent.relative_to(input_directory)
        (output_directory / relative_dir).mkdir(parents=True, exist_ok=True)

        compress_image(file_path, output_directory / relative_dir, compression_quality=desired_compression_quality) # specified quality

        # progress
        percentage = (counter + 1) * 100 / total_files
        print(f"Progress: {percentage:.2f}%")

if __name__ == "__main__":
    main()
