Here's the strategy!

1. Threshold images to produce binary image
2. Remove lines through smoothing algorithm (for each pixel, make a box
	and if the majority of the pixels are white, smooth to white)
3. Use a Dirichlet process model to cluster each of the heads of the notes
4. Draw boxes around the notes to catch the stems.
5. Some sort of learning algorithm to determine what note it is????


