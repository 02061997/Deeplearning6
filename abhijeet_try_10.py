# -*- coding: utf-8 -*-
"""Abhijeet_Try_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nDSnr-ksyhzznGJRuzE53wb2W16aYxQp
"""

from google.colab import drive
drive.flush_and_unmount()

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive 
drive.mount('/content/gdrive')
# %cd /gdrive

import os      
import zipfile


local_zip = '/content/gdrive/MyDrive/Data_set_H.W5/ASSIGNMENT5_DATA_SET_2.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content/gdrive/MyDrive/ass_5_dataset/')
zip_ref.close()

import os
base_dir = '/content/gdrive/MyDrive/ass_5_dataset/ASSIGNMENT5_DATA_SET'
train_dir = os.path.join(base_dir, 'Train')
validation_dir = os.path.join(base_dir, 'Validation')
print(os.listdir(base_dir))

# Directory with our training pictures
train_abhi_dir = os.path.join(train_dir, 'ABHIJEET-AIRPODS_DL5')
train_apple_dir = os.path.join(train_dir, 'APPLE_DL5')
train_clock_dir = os.path.join(train_dir, 'CLOCK_DL5')
train_lamp_dir = os.path.join(train_dir, 'LAMP_DL5')
train_laptop_dir = os.path.join(train_dir, 'LAPTOP_DL5')
train_notepad_dir = os.path.join(train_dir, 'NOTEPAD_DL5')
train_napkin_dir = os.path.join(train_dir, 'PAPERNAPKIN_DL5')
train_shru_dir = os.path.join(train_dir, 'SHRUTI-AIRPOD_DL5')
train_speaker_dir = os.path.join(train_dir, 'SPEAKER_DL5')
train_uno_dir = os.path.join(train_dir, 'UNO_DL5')

# Directory with our validation pictures
validation_abhi_dir = os.path.join(validation_dir, 'ABHIJEET-AIRPODS_DL5')
validation_apple_dir = os.path.join(validation_dir, 'APPLE_DL5')
validation_clock_dir = os.path.join(validation_dir, 'CLOCK_DL5')
validation_lamp_dir = os.path.join(validation_dir, 'LAMP_DL5')
validation_laptop_dir = os.path.join(validation_dir, 'LAPTOP_DL5')
validation_notepad_dir = os.path.join(validation_dir, 'NOTEPAD_DL5')
validation_napkin_dir = os.path.join(validation_dir, 'PAPERNAPKIN_DL5')
validation_shru_dir = os.path.join(validation_dir, 'SHRUTI-AIRPOD_DL5')
validation_speaker_dir = os.path.join(validation_dir, 'SPEAKER_DL5')
validation_uno_dir = os.path.join(validation_dir, 'UNO_DL5')

#verify the first 10 frams name list 
train_abhi_fnames = os.listdir(train_abhi_dir)
print(train_abhi_fnames[:10])

train_apple_fnames = os.listdir(train_apple_dir)
print(train_apple_fnames[:10])

train_clock_fnames = os.listdir(train_clock_dir)
print(train_clock_fnames[:10])

train_lamp_fnames = os.listdir(train_lamp_dir)
print(train_lamp_fnames[:10])

train_laptop_fnames = os.listdir(train_laptop_dir)
print(train_laptop_fnames[:10])

train_notepad_fnames = os.listdir(train_notepad_dir)
print(train_notepad_fnames[:10])

train_napkin_fnames = os.listdir(train_napkin_dir)
print(train_napkin_fnames[:10])

train_shru_fnames = os.listdir(train_shru_dir)
print(train_shru_fnames[:10])

train_speaker_fnames = os.listdir(train_speaker_dir)
print(train_speaker_fnames[:10])

train_uno_fnames = os.listdir(train_uno_dir)
print(train_uno_fnames[:10])

# Adding rescale, rotation_range, width_shift_range, height_shift_range,
# shear_range, zoom_range, and horizontal flip to our ImageDataGenerator
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,)


val_datagen = ImageDataGenerator(rescale=1./255)

# Flow training images in batches of 30 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        train_dir,  # This is the source directory for training images
        target_size=(224,224),  # All images will be resized to 224x224
        batch_size=30,
        class_mode='categorical')

# Flow validation images in batches of 30 using val_datagen generator
validation_generator = val_datagen.flow_from_directory(
        validation_dir,
        target_size=(224,224),
        batch_size=5,
        class_mode='categorical')

import keras
from keras.layers import Dense, Dropout
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import tensorflow as tf

model = tf.keras.models.Sequential([
  
  tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(224,224,3)),
  tf.keras.layers.MaxPooling2D(2,2),

  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),      

  tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),    

  tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2), 


  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.5),

  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation= 'softmax')                 
                                    
])

from tensorflow.keras.optimizers import RMSprop

model.compile(loss='categorical_crossentropy',
              optimizer='RMSprop',
              metrics=['accuracy'])

model.summary()

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard


from datetime import datetime
from packaging import version

import tensorflow as tf
from tensorflow import keras


import numpy as np

logdir = 'logs\object' + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)

object_names=['UNO_DL5', 'ABHIJEET-AIRPODS_DL5', 'NOTEPAD_DL5', 'CLOCK_DL5', 'PAPERNAPKIN_DL5', 'LAPTOP_DL5', 'APPLE_DL5', 'LAMP_DL5', 'SPEAKER_DL5', 'SHRUTI-AIRPOD_DL5']
object_ids = list(range(10))
classes=dict(zip(object_names,object_ids))
classes

import keras
from keras.preprocessing import image
import numpy as np
from numpy import asarray
from keras.preprocessing.image import img_to_array
from keras.applications.resnet50 import preprocess_input

def get_image_predict(image_file_name):
  im=image.load_img(image_file_name,target_size=(224,224))
  im=image.img_to_array(im)
  im=np.expand_dims(im,axis=0)
  im=preprocess_input(im)
  image_feature=model.predict(im)[0]
  image_features=np.asarray(image_feature)

  return image_features

history = model.fit(
      train_generator,
      steps_per_epoch=20,
      epochs=20,
      validation_data=validation_generator,
      validation_steps=4,
      verbose=1,
      callbacks=[tensorboard_callback]
)

image_predict=get_image_predict('/content/jbl.JPG')
prediction_idx=np.argmax(image_predict)
print(image_predict)
object_names[prediction_idx]

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs/object

model_reduced = keras.Sequential()

for layer in model.layers[:-1]:
  model_reduced.add(layer)
model_reduced.summary()

import cv2
import os, argparse
import pickle
from keras.preprocessing import image
import numpy as np
from numpy import asarray
from keras.preprocessing.image import img_to_array

data_path = '/content/gdrive/MyDrive/ass_5_dataset/ASSIGNMENT5_DATA_SET/Train'
data_dir_list = os.listdir(data_path)
image_features_list=[]
image_name_feature=[]

def get_image_features(image_file_name):
  im=image.load_img(image_file_name,target_size=(224,224))
  im=image.img_to_array(im)
  im=np.expand_dims(im,axis=0)
  im=preprocess_input(im)
  image_feature=model_reduced.predict(im)[0]
  image_features_arr=np.asarray(image_feature)

  return image_features_arr

for dataset in data_dir_list:
  img_list=os.listdir(data_path+'/'+ dataset)
  print('EXTRACTING FEATURES OF DATASET-'+'{}\n'.format(dataset))
  for img in img_list:
  
        img_path=data_path + '/'+ dataset + '/'+ img 
        image_features=get_image_features(img_path)
      
        image_features_list.append(image_features)
        image_name_add=[img,image_features]
        image_name_feature.append(image_name_add)
    
image_features_arr = np.asarray(image_features_list)
image_features_arr = np.rollaxis(image_features_arr,1,0)
image_features_arr = image_features_arr.T


np.savetxt('/content/gdrive/MyDrive/ass_5_dataset/embedding-logs/feature_objects10.txt', image_features_arr)
pickle.dump(image_features_arr, open('/content/gdrive/MyDrive/ass_5_dataset/embedding-logs/feature_objects10.pkl', 'wb'))

import os,cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
import tensorflow as tf
from tensorboard.plugins import projector
tf.__version__

LOG_DIR = '/content/gdrive/MyDrive/ass_5_dataset/embedding-logs'
tf.compat.v1.disable_eager_execution()

img_data = []
for dataset in os.listdir(train_dir):
  img_list = os.listdir(train_dir + '/'+dataset)
  print('Loaded the images of dataset - ' + '{}'.format(dataset))
  for img in img_list:
    
    input_img = cv2.imread(train_dir + '/'+ dataset+'/'+img)
    input_img_resize=cv2.resize(input_img,(224,224))
    img_data.append(input_img_resize)

img_data = np.array(img_data)

feature_vectors = np.loadtxt(os.path.join(LOG_DIR,'feature_objects10.txt'))
print ("feature_vectors_shape:",feature_vectors.shape)
print ("num of images:",feature_vectors.shape[0])
print ("size of individual feature vector:",feature_vectors.shape[1])

num_of_samples = feature_vectors.shape[0]
num_of_samples_each_class = 60
features = tf.Variable(feature_vectors,name = 'features')
y = np.ones((num_of_samples,),dtype='int64')
y[0:60] =0,
y[60:120] = 1,
y[120:180] = 2,
y[180:240] = 3,
y[240:300] = 4,
y[300:360] = 5,
y[360:420] = 6,
y[420:480] = 7,
y[480:540] = 8,
y[540] = 9

names=['ABHIJEET-AIRPODS_DL5','APPLE_DL5','CLOCK_DL5','LAMP_DL5','LAPTOP_DL5','NOTEPAD_DL5','PAPERNAPKIN_DL5','SHRUTI-AIRPOD_DL5','SPEAKER_DL5','UNO_DL5']

metadata_file = open(os.path.join(LOG_DIR, 'metadata_10_classes.tsv'), 'w')
metadata_file.write('Class\tName\n')
k=60
j=0
for i in range(num_of_samples):
  c = names[y[i]]
  if i%k==0:
    j=j+1
  metadata_file.write('{}\t{}\n'.format(j,c))
metadata_file.close()

def images_to_sprite(data):
    
    if len(data.shape) == 3:
        data = np.tile(data[...,np.newaxis], (1,1,1,3))
    data = data.astype(np.float32)
    min = np.min(data.reshape((data.shape[0], -1)), axis=1)
    data = (data.transpose(1,2,3,0) - min).transpose(3,0,1,2)
    max = np.max(data.reshape((data.shape[0], -1)), axis=1)
    data = (data.transpose(1,2,3,0) / max).transpose(3,0,1,2)

    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = ((0, n ** 2 - data.shape[0]), (0, 0),
            (0, 0)) + ((0, 0),) * (data.ndim - 3)
    data = np.pad(data, padding, mode='constant',
            constant_values=0)
    # Tile the individual thumbnails into an image.
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3)
            + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    data = (data * 255).astype(np.uint8)
    return data

sprite = images_to_sprite(img_data)
cv2.imwrite(os.path.join(LOG_DIR, 'sprite_10_classes.png'), sprite)

with tf.compat.v1.Session() as sess:
    saver = tf.compat.v1.train.Saver([features])

    sess.run(features.initializer)
    saver.save(sess, os.path.join(LOG_DIR, 'images_10_classes.ckpt'))
    
    config = projector.ProjectorConfig()
    embedding = config.embeddings.add()
    embedding.tensor_name = features.name
    embedding.metadata_path = os.path.join(LOG_DIR, 'metadata_10_classes.tsv')
    embedding.sprite.image_path = os.path.join(LOG_DIR, 'sprite_10_classes.png')
    embedding.sprite.single_image_dim.extend([img_data.shape[1], img_data.shape[1]])
    projector.visualize_embeddings(tf.compat.v1.summary.FileWriter(LOG_DIR), config)

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir='/content/gdrive/MyDrive/ass_5_dataset/embedding-logs' --port=5005

