#Metodos de captura de imagenes ##########################################################################

import cv2
import uuid

import numpy as np


"""
	En este caso, 0 quiere decir que queremos acceder
	a la cámara 0. Si hay más cámaras, puedes ir probando
	con 1, 2, 3...
"""
cap = cv2.VideoCapture(0)

leido, frame = cap.read()
nombre_foto=""
if leido == True:
	nombre_foto = str(uuid.uuid4()) + ".png" # uuid4 regresa un objeto, no una cadena. Por eso lo convertimos
        #('C:\\Users\\admin\\Pictures\\Camera Roll') se debe especificar ruta completa, se recomienda test/test/
	cv2.imwrite(nombre_foto, frame)
    
	print("Foto tomada correctamente con el nombre {}".format(nombre_foto))
else:
	print("Error al acceder a la cámara")

"""
	Finalmente liberamos o soltamos la cámara
"""
print(nombre_foto)
imagen = cv2.imread(nombre_foto) 
cv2.imshow('Logo OpenCV',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap.release()
###cambiamos la imgagen a escala de grises
gray_img=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
cv2.imshow("escalada",gray_img)
#generamos la imagen binaria
_,thresh=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Bynari",thresh)
#detencion de contornos
img_contorno=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
img_contorno=sorted(img_contorno,key=cv2.contourArea)
for i in img_contorno:
    if cv2.contourArea(i)>100:
        break

#genreamos la mascara
mask=np.zeros(imagen.shape[:2],np.uint😎
#dibujar contornos
cv2.drawContours(mask,[i],-1,255,-1)
#Subtraccion del fondo
new_imagen=cv2.bitwise_and(imagen,imagen,mask=mask)
#mostrar resultado
cv2.imshow("sin fondo",new_imagen)
# modificando la imagen para ser almacenada en formato compatible

img = imagen

print('Original Dimensions : ',img.shape)

width = 100
height = 100
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print('Resized Dimensions : ',resized.shape)

cv2.imshow("Resized image", resized)
cv2.imwrite("Resized image.png", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Cierre de los metodos de captura para la imagen #############################


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import tensorflow as tf 
import os 
import matplotlib.image as mpimg

import random
from keras import layers
from keras.preprocessing.image import ImageDataGenerator 
from sklearn.model_selection import train_test_split 
from keras.utils import load_img, img_to_array
import pathlib
import numpy as np

for dirpath, dirnames, filenames in os.walk("C:\\Users\\juand\\Downloads\\archive\\"):
    print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")


train_path = "train/train/"
test_path = "test/test/"

# Get the class names (programmatically, this is much more helpful with a longer list of classes)
data_dir = pathlib.Path(train_path) # turn our training path into a Python path
class_names = np.array(sorted([item.name for item in data_dir.glob('*')])) # created a list of class_names from the subdirectories
print(class_names)

# View an image
def view_random_image(target_dir, target_class):
  # Setup target directory (we'll view images from here)
  target_folder = target_dir+target_class

  # Get a random image path
  random_image = random.sample(os.listdir(target_folder), 100)

  # Read in the image and plot it using matplotlib
  img = mpimg.imread(target_folder + "/" + random_image[0])
  plt.imshow(img)
  plt.title(target_class)
  plt.axis("off");

  return img

plt.figure(figsize = (15,10))
# View a random image from the training dataset for all classes
for i in range(33):
    plt.subplot(5,8,i+1)
    img = view_random_image(target_dir=train_path,
                        target_class=class_names[i])
    

train_val_data = {'path' : [],
       'filename': [],
       'label': []}
for dirpath, dirnames, filenames in os.walk(train_path):
    for f in filenames:
        train_val_data['path'].append(dirpath)
        train_val_data['filename'].append(f)
        train_val_data['label'].append(f.split('_')[0])

train_val_data_df = pd.DataFrame(train_val_data)
train_val_data_df.head()

#Read test data and create a dataframe
test_data = {'path' : [],
       'filename': []}
for dirpath, dirnames, filenames in os.walk(test_path):
    for f in filenames:
        test_data['path'].append(dirpath)
        test_data['filename'].append(f)

test_data_df = pd.DataFrame(test_data)
test_data_df.head()

plt.figure(figsize = (15,6))
#data_df['label'].value_counts().plot(kind='barh')
sns_cntplot = sns.countplot(x='label', data=train_val_data_df)
plt.xticks(rotation=45);

images = []
label = [] 

for _, d in train_val_data_df.iterrows():
    img = load_img(os.path.join(d['path'],d['filename']))
    images.append(img_to_array(img))
    label.append(d['label'])

images = np.array(images)
labels = np.array(label)
print(f"Complete data images shape: {images.shape} and label shape: {labels.shape}")

test_images = []

for _, d in test_data_df.iterrows():
    img = load_img(os.path.join(d['path'],d['filename']))
    test_images.append(img_to_array(img))
    
test_images = np.array(test_images)
print(f"Test images shape: {test_images.shape} ")

class_indices = dict(zip(class_names, range(len(class_names))))

labels_encoded = list(map(class_indices.get, labels))

#Convert to categorical data using tensorflow 
#labels to One-hot encoded
label_categorical = tf.keras.utils.to_categorical(labels_encoded, num_classes=len(class_names), dtype='uint8')

train_im, valid_im, train_lab, valid_lab = train_test_split(images, label_categorical, test_size=0.20, 
                                                            stratify=label_categorical, 
                                                            random_state=40, shuffle = True)

print ("train data shape after the split: ", train_im.shape)
print ('new validation data shape: ', valid_im.shape)
print ("validation labels shape: ", valid_lab.shape)

print ('train im and label types: ', type(train_im), type(train_lab))

training_data = tf.data.Dataset.from_tensor_slices((train_im, train_lab))
validation_data = tf.data.Dataset.from_tensor_slices((valid_im, valid_lab))
test_data = tf.data.Dataset.from_tensor_slices(test_images)

print ('check types; ', type(training_data), type(validation_data), type(test_data))

### check using element_spec

print (training_data.element_spec)
print (validation_data.element_spec)

### as expected, tensors of image and original label shape


### create an iterator and turn it into numpy array 
train_iter = iter(training_data)
print(next(train_iter)[0].numpy(), '\n', next(train_iter)[1].numpy(), np.argmax(next(train_iter)[1].numpy()))

train_iter_im, train_iter_label = next(iter(training_data))
print (train_iter_im.numpy().shape, train_iter_label.numpy().shape)

train_iter_im1, train_iter_label1 = next(training_data.as_numpy_iterator())
print (train_iter_im1.shape, train_iter_label1.shape)

check_list = list(training_data.as_numpy_iterator())
print (len(check_list), check_list[1])

fig = plt.figure(figsize=(10,10))
for i in range(12):
    plt.subplot(4,3,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(check_list[i][0]/255.)
    plt.xlabel(class_names[np.argmax(check_list[i][1])], fontsize=13)
plt.tight_layout()    
plt.show()

rescale_data = tf.keras.Sequential([
    #layers.experimental.preprocessing.Rescaling(1/255)
    
])

data_augmenation = tf.keras.Sequential([
    #layers.experimental.preprocessing.RandomFlip(mode = "horizontal"),
    #layers.experimental.preprocessing.RandomRotation(0.1)
])

random_image_index = random.randint(0,len(train_im))
img = rescale_data(train_im[random_image_index])
img = data_augmenation(img)
plt.imshow(img)

BATCH_SIZE = 128 
AUTOTUNE = tf.data.AUTOTUNE 

def prepare(ds, shuffle=False, augment = False, test = False):
    if test:
        ds = ds.map(lambda x: (rescale_data(x)), num_parallel_calls=AUTOTUNE)
    else:
        ds = ds.map(lambda x, y: (rescale_data(x), y), num_parallel_calls=AUTOTUNE)
    
    if shuffle:
        ds = ds.shuffle(1000)
    
    #batch the data 
    ds = ds.batch(BATCH_SIZE)
    
    # Use data augmentation only on the training set.
    if augment:
        ds = ds.map(lambda x, y: (data_augmenation(x, training=True), y), 
                num_parallel_calls=AUTOTUNE)
    
    # Use buffered prefetching on all datasets.
    return ds.prefetch(buffer_size=AUTOTUNE)

train_ds = prepare(training_data, shuffle = True, augment = True)
val_ds = prepare(validation_data)
test_ds = prepare(test_data, test=True)

model_1 = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=5, 
                          kernel_size = 3,
                          activation = "relu",
                          input_shape = (100,100,3)),
    tf.keras.layers.MaxPool2D(pool_size =2,
                             padding='valid'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(len(class_names), activation="softmax")
])

model_1.compile(loss="categorical_crossentropy",
               optimizer = tf.keras.optimizers.Adam(),
               metrics = ['accuracy'])

model_1.summary()

#Fit the model on training data 
history_1 = model_1.fit(train_ds,
                       epochs =5,
                       validation_data= val_ds)

model_1.evaluate(val_ds)

#loss and accuracy plot 
pd.DataFrame(history_1.history).plot()

y_pred = model_1.predict(val_ds)
y_pred[:1]


y_pred.shape  #shape of y_pred
y_pred = tf.argmax(y_pred, axis=1) # Get y_pred classes 
y_true = np.argmax(valid_lab,axis=1)
y_true, y_pred
len(y_pred), len(y_true)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
cm

plt.figure(figsize = (15,15))
sns.heatmap(pd.DataFrame(cm, index= class_names, columns = class_names), annot = True, cmap="Blues")

predictions = model_1.predict(test_ds)
predictions.shape
predictions = class_names[tf.argmax(predictions, axis=1)] # Get classes 
predictions[:5]
predictions.shape

submission = pd.read_csv("C:\\Users\\juand\\Downloads\\archive\\sampleSubmission.csv")
submission.head(2)

test_data_df.head() # We already have this data. lets take filename from this

submission['id'] = test_data_df['filename']
submission['label'] = predictions
submission.head()
submission.to_csv("submission.csv",index=False)
