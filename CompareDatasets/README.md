<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>
  <h1>Duplicated Images Checker</h1>
  <p>This Python script checks for duplicated images or files in two datasets by comparing their hashes and deletes the duplicates from the new dataset.</p>

  <h2>Usage</h2>
  <ol>
    <li>Place the Python script in the same directory as the two datasets.</li>
    <li>Run the script using the command: <code>python duplicated_images_checker.py</code></li>
    <li>The script will compare the hashes of the files in the two datasets and delete any duplicates found in the new dataset.</li>
  </ol>

  <h2>How it works</h2>
  <p>The script performs the following steps:</p>
  <ol>
    <li>Iterates through the files in the source dataset and calculates their hashes.</li>
    <li>Iterates through the files in the new dataset and calculates their hashes.</li>
    <li>Compares the hashes of the files in the two datasets.</li>
    <li>If a duplicate is found, the file is deleted from the new dataset.</li>
  </ol>

  <h2>Notes</h2>
  <ul>
    <li>Make sure to backup your datasets before running the script, as it will delete files from the new dataset.</li>
    <li>The script assumes that the files in the datasets are images or files with unique hashes. If two different files have the same hash, one of them will be considered a duplicate and deleted.</li>
  </ul>
</body>
</html>
