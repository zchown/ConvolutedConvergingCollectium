### Current Issues
    * Generated Images still look very skeletal
    * Generated Images have pixelated squarish look to the generated areas
    * Color issues

### Things to try for the future
    * Adjust LAMBDA values to punish model more or less for how connected the generated image is to the skeleton
    * Reduce the input image to grayscale and also compare the generated image to the grayscale image
        * Maybe can help with the color issues
    * What is the best batch size
    * What is the best learning rate
    * What is the best size for the images to be in
    * Can we use the skeleton2animal models? They are using pix2pix so maybe we can use them for our generator and discriminator and then train on a new dataset


### Data
    * Some of the images are not the best quality for what we are trying to do
        * Images with the outline of the animal already in them
        * Different background colors
    * See if we can web scrape more images to get a larger dataset

