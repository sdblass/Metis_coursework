# Bird Species Image Classifier
## Objective
The technological revolution has brought unprecedented wealth to impoverished nations, however, at a cost to natural avian wildlife. Many bird species are being added to the endangered species as a result of encroachment of civilization into virgin forests and disruptions of mating and migratory patterns. Ornithologists and conservationists need to be able to study bird behavior in order to measure the impact civilization is having on bird populations. However, many areas containing a rich diversity of species are difficult to access and can only be reached by foot after hiking for days. Researchers would benefit from having the ability to study birds from images sent by satellite-enabled webcams in remote locations.

The objective of this project is to create an image classifier that identify species of birds in images taken by webcams. Researchers would be able to then study bird sightings by location, time of day, season, and presence of other birds.


## Design
Three categories of image classifier models are covered in this project to show how increasing the complexity of the model leads to improved accuracy. 
* Logistic regression
* Basic convolutional neural network
* Transfer learning

The baseline logistic regression model was incapable of any meaningful prediction so a convolutional neural network was implemented instead.

The notebooks in this project illlustrate how accuracy of the validation data improves increasing the number of training images and when augmenting the images by horizontally flipping (birds do not usually fly upside down) and rotating. 

## Data

The data come from [Kaggle](https://www.kaggle.com/datasets/gpiosenka/100-bird-species). 

_Data metrics:_
* Number of species: 400
* Pixel count: 224X224X3
* Color: RBG
* Format: jpg
* Number of training images: 58,388
* * Number of validation images: 2000 (5 per species)
* Test: 2000 (5 per species)

![Examples of birds](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/images/birds.png)


## Algorithms


### Exploratory data anlysis
Bird species were ranked by number of training images available and species with the greatest number of training images were selected. Due to memory restrictions, a maximum of 50 classes were modeled when implementing transfer learning. More basic models that were entirely trained from scratch were limited to 4 classes. The classes were chosen by selecting the bird species with the greatest number of training images available.

### Baseline model (logistic regression)
Each training image was transformed into a 1D vector containing RGB pixel values and assembled into a 827 x 150,528 matrix for 827 training images. The matrix was reduced to a 827x2 matrix via truncated SVD and fed to a logistic regression model.

### Basic convolutional neural network
Alternating layers of convolutions and max pooling followed by a flatten layer, dropout, and two dense layers connected to an output.

### Transfer learning
* VGG16
* ResNet

## Tools
* Data acquisition: Kaggle
* Analysis: Google Colab, pandas, keras, sklearn
* Visualization: matplotlib, seaborn

## Communication
* Slides, visuals, write-up

## Results

### Poor results with baseline model
Logistic regression accuracy was unable to distinguish bird species by a vector representation of the images. Therefore, a more sophisticated model was required.

As shown below, logistic regression is unable to separate 5 classes and so obtains an accuracy of 32%. As the number of species is increased more dots appear on the chart and drawing lines to separate the dots into distinct classes becomes even harder so the accuracy decreases.

![logreg]()

### Factors that improve the basic CNN model

Image augmentation by flipping and rotating the training images improved the validation accuracy. Increasing the batch size reduced the tendency of the model to overfit the training data. By the end of 30 epochs, the validation accuracy was around 95% for 4 classes. Applying the model to more than 4 classes was possible but memory issues began to arise at around 10 classes so the bulk of the work was limited to 4 classes.

![basicCNN](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/images/SVD.png)

While good results are possible with a basic CNN model, the best case scenario can be obtained when leveraging pretrained models through transfer learning.

### Transfer learning
VGG16 and ResNet were implemented and both models achieved results for 50 classes that were far superior than the basic CNN models in fewer epochs. Transfer learning models represent best-case scenarios where we have a great deal of resources to thoroughly train a model on image recognition.

**VGG**
![VGG](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/images/vgg16.png)

**ResNet**
![ResNet](https://github.com/sdblass/Metis_coursework/blob/master/6_Deep_Learning/images/resnet.png)