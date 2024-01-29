file_name=str(input("File name: "))
media_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/txt",
    "zip": "application/zip"
}
suffix=""
if "." in file_name:
    suffix=file_name.split(".")[-1]d

mt=media_types.get(suffix,"application/octet-stream")
print(mt)
    