# Bird Species Image Classifier

## Objective
The goal of this project is to create a neural network that classifies bird species. A functioning classifier could help scientists study bird patterns of life by gathering data from webcams in remote locations.

## Solution Path
The data set contains 400 species with up to 249 training images and 5 validation images per species.

[example image](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/MVP/001.jpg)

[species_count](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/MVP/species_count.png)

This project will study three ways of building an image classifier.
* Logistic regression
* Basic convolutional neural network
* Transfer learning

## Current Progress
### Work status

#### Logistic regression
A simple logistic regression is complete. Each image was converted to a 1D vector containing RGB pixel values. Due to the size of the resulting matrix, the reuslts were limited to 5 species. The 827x150,528 matrix was converted to 827x2 using Truncated SVD (sklearn) and plotted.

[SVD](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/MVP/SVD.png)

There does appear to be some separation in that no color occupies all other colors. Green dots appear at the top, blue dots at the bottom, purple in the middle, and orange overlaps them all. The accuracy is 32% so a CNN will need to beat this number. The accuracy drops to 15% when increasing the number of species to 15. It is possible that many bird species look alike so adding additional species only serves to confuse the model.

#### CNN
A CNN was created containing 4 convolutional layers interchanged with 4 max pool layers, a layer that converts the data to 1D vectors, a dropout layer to regularize the model, and two dense layers.

The model was tested for 2 and 4 classes with and without image augmentation (horizontal flipping and rotation up to 45 degrees). The accuracy improved with image augmentation and more classes.

[2_classes](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/MVP/2_classes_acc.png)
[4_classes](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/MVP/4_classes_acc.png)

### Next steps
* Add another regularization into the network. The fluctuation in the validation accuracy could be a sign that the model is overfitting.
* Try 6 classes to see if improvements continue with adding classes. At 10 classes, the model threw a warning so there is probably a limit to the number of classes we can analyze using this basic model.
* Turn to transfer learning.
