import copy
import os.path

import matplotlib.pyplot as plt
from pydicom.filereader import dcmread
from pydicom.pixels import pixel_array
from pydicom import examples

# path = r'/home/labcc/AlvesSource/OpenDect/debug_example/series-00000'
# file = 'image-00000.dcm'
# filename = os.path.join(path, file)
#
# data = dcmread(filename)
#
# print()


# # Get an example dataset as a FileDataset instance
# ds = examples.ct
#
# # Convert the pixel data to a ndarray
# arr = pixel_array(ds)
# assert arr.shape == (128, 128)
# assert str(arr.dtype) == "int16"


# Get an example multi-frame dataset
# ds = examples.rt_dose
# path = examples.get_path("rt_dose")
path = r'/home/labcc/AlvesSource/OpenDect/debug_example'
ds = dcmread(os.path.join(path, 'rtdose.dcm'))
print(path)
assert ds.NumberOfFrames == '15'

# Return all frames
arr = pixel_array(ds)
assert arr.shape == (15, 10, 10)

# new_arr = copy.deepcopy(arr)
# new_arr[0:5, 0:5, :] = 8 * 10 ** 5
# new_arr[0:5, 5:, :] = 12 * 10 ** 5

new_arr = copy.deepcopy(arr) + 4 * 10 ** 7
ds.PixelData = new_arr.tostring()
# update the information regarding the shape of the data array
ds.Rows, ds.Columns = new_arr.shape[1:]

# print the image information given in the dataset
print('The information of the data set after downsampling: \n')
print(ds)
print(ds.pixel_array)
print(len(ds.PixelData))
ds.save_as(os.path.join(path, 'high_modified_rtdose.dcm'))

# Return only the first frame
arr = pixel_array(ds, index=4)

# Display the pixel data using matplotlib
plt.imshow(arr, cmap="gray")
plt.show()
