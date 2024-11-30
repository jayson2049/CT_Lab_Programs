import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt

image_path = "/home/prithvi/Downloads/image-00001.dcm"
ds = dicom.dcmread(image_path)
plt.imshow(ds.pixel_array)

plt.show()
