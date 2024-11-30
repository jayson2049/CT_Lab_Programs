import pydicom
file_path = "/home/prithvi/Downloads/image-00001.dcm"
medical_image = pydicom.read_file(file_path)
print(medical_image)
