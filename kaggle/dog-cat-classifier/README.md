
# Cats vs Dogs classifier from finetuning VGG using AWS
This is my personal project for week1 of the fast.ai online course. The helper files (utils.py, vgg16.py) are from the course, and were not written by me. I used Keras, with a pretrained convolutional neural net.

This is my first project using AWS. I'm using a p2.xlarge EC2 instance for final training (GPU accelerated) and a t.large EC2 instance for initial coding and testing. I figured out how to have a single EBS storage volume shared between the two instances, so I could easily do the work without incurring any more costs than necessary. I set up some aliases in bash to help keep my workflow simple. I've included the bash code in the notebook as well.

# Conclusion
My final score was about .094, putting me at 402 out of 1316. Not amazing, but a top 31% score is satisfactory for now.

### Ideas for improving:

more epochs. With 1 epoch my prediction accuracy in the training/validation sets is 98%+, but I could do a few more epochs to see if that helps.

error analysis. Which images are being incorrectly categorized? In particular, which are given a very high probability score for the wrong category? If there's a pattern to the mistakes, I could get a few thousand more images similar to the wrongly classified images and see if that helps.

More images in general: I trained off 25,000 images. There's an easily accessable image set of cats and dog pictures. It took about 5 minutes to train on the 25,000 images, so I could conceivably get another 300,000 images to train on for an hour of extra computation time. ($.90 on AWS)

the VGG architecture is a little out of date at this point. A much higher score might require a better CNN architecture. If I attempt to raise my score from here, I don't intend to use VGG.
