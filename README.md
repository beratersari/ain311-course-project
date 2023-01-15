# ain311-course-project
AIN311 CLASS COURSE PROJECT

Current Status:

We made finetuning on the TQuAD dataset. We are clering the code of the training and inferencing. After that, we will upload these codes.

Done:

----> Dataset preparing codes are uploaded

----> Score Calculation script added

----> Train code is uploaded for mT5 model

----> Inference code will be uploaded

To Do:







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
python make_dataset_csv.py
```

Then your dataset created in the dataset folder. Go to the mT5 folder and the change the directories in the config file. Also, you can change the hyperparameters of the model. After that operation run the following command.

```
python train.py
```

For evaluation

```
python test.py
```

##### Note
If you don't want to install the librares on your local computer. Just upload the jpnyb file to the kaggle and enable the gpu of the kaggle notebook. Then run the code blocks sequentially.



We benefited from a kaggle notebook while preparing the training code, that fine-tune the mT5 model for Hindi Language. 

