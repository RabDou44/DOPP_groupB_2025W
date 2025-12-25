import kagglehub
import os
import shutil

def download_flight_data():
    print("Starting download from Kaggle...")
    download_path = kagglehub.dataset_download("polartech/flight-data-with-1-million-or-more-records")
    
    print(f"Files downloaded to cache: {download_path}")

    target_directory = "data"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"Created directory: {target_directory}")

    files_found = 0
    for filename in os.listdir(download_path):
        if filename.lower().endswith(('.csv', '.zip')):
            source_file = os.path.join(download_path, filename)
            destination_file = os.path.join(target_directory, filename)
            
            shutil.copy(source_file, destination_file)
            print(f"Successfully saved: {filename}")
            files_found += 1

    print("-" * 30)
    print(f"Done! {files_found} file(s) are now in the '{target_directory}' folder.")

if __name__ == "__main__":
    download_flight_data()