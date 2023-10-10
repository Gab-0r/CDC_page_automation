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

