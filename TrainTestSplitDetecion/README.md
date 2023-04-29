<!DOCTYPE html>
<html>
<head>
	<title>Split Images and Labels</title>
</head>
<body>
	<h1>Split Images and Labels</h1>
	<p>This script splits the images and labels into training and validation sets. It moves the validation images and labels to separate folders.</p>
	<h2>Usage</h2>
	<p>To use this script, follow these steps:</p>
	<ol>
		<li>Clone the repository to your local machine.</li>
		<li>Install the required libraries using the following command:</li>
	</ol>
	<pre><code>pip install tqdm</code></pre>
	<ol start="3">
		<li>Place your images in the <code>images/</code> folder and your labels in the <code>labels/</code> folder.</li>
		<li>Open the <code>split_images_and_labels.py</code> file and edit the <code>threshold</code> value as desired.</li>
		<li>Run the script using the following command:</li>
	</ol>
	<pre><code>python split_images_and_labels.py</code></pre>
	<h2>License</h2>
	<p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>
</body>
</html>
