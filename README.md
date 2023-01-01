# ain311-course-project
AIN311 CLASS COURSE PROJECT

Current Status:

We made finetuning on the TQuAD dataset. We are clering the code of the training and inferencing. After that, we will upload these codes.

Done:

----> Dataset preparing codes are uploaded

----> Score Calculation script added

----> Train code is uploaded for mT5 model

To Do:

----> Inference code will be uploaded

----> A scrapper script will be uploaded to get random data from twitter. And we will test the model on non-offical language.





# Installation for fine-tuning mT5:

You have to install listed libraries to run the train and eval files. Also, you have to download other necessary libraries (torch, numpy, pandas) on your own. But, the listed ones and theirs versions are important
```
!pip install pytorch_lightning==0.8.1
!pip install transformers==4.0.0rc1
!pip install -U nltk
!pip install rouge_score
```

# How to use the repository

After the installation of the dataset. Just modify the config file. Adjust the path of your json file and get the csv data. By running following command.
```
python 
```


