from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os


def upload_file_to_blob(file_name):
    account_name = os.getenv("ACCOUNT_NAME")
    account_key = os.getenv("ACCOUNT_KEY")
    container_name = os.getenv("CONTAINER_NAME")

    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net",
                                            credential=account_key)
    container_client = blob_service_client.get_container_client(container_name)

    folder_path = "reference_refined/cdc/"
    file_path= f"downloads/{file_name}"

    # Combine the folder path and file name to form the blob name
    blob_name = folder_path + file_name

    # Upload the file to the specified blob
    blob_client = container_client.get_blob_client(blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)


def clean_downloaded_file(input_file_name: str, output_file_name: str):
    # Define the input file and output file paths
    input_file_path = os.getcwd() + f"/downloads/{input_file_name}"
    output_file_path = os.getcwd() +  f"/downloads/{output_file_name}"
    # Initialize a flag to indicate when to stop reading lines
    stop_reading = False
    # Open the input and output files
    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        # Loop through each line in the input file
        for line in input_file:
            # Check if the "---" delimiter is found
            if "---" in line:
                # Set the flag to stop reading
                stop_reading = True
            # Check if we should stop reading lines
            if not stop_reading:
                # Write the line to the output file
                output_file.write(line)
    # Close the input and output files
    input_file.close()
    output_file.close()

