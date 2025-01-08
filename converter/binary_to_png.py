from io import BytesIO
import base64
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image

def upload_image_from_byte_image_array(byte_array, file_name):
    # Convert the byte array to a file object
    decoded_byte_array = base64.b64decode(byte_array)
    byte_stream = BytesIO(decoded_byte_array)
    image = Image.open(byte_stream)
    # Saving image file in memory
    bytes_io_image_file = BytesIO()
    image.save(bytes_io_image_file, format= image.format)
    bytes_io_image_file.seek(0)

    # Creating in InmemoryuploadFile Instance
    memory_file = InMemoryUploadedFile(file=bytes_io_image_file,
        field_name=None,
        name=file_name,
        content_type=f'image/{image.format.lower()}',
        size=sys.getsizeof(bytes_io_image_file),
        charset=None,
        content_type_extra=None,)
    
    return memory_file

