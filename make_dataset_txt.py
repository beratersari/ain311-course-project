import json
import os
import config
class TQuadDataset:
    def __init__(self):
        f=  open(config.train_data_path)
        self.train_data = json.load(f)
        self.train_data=self.train_data["data"]
        f=  open(config.dev_data_path)
        self.dev_data= json.load(f)
        self.dev_data=self.dev_data["data"]
    def print_data(self):
        for index in range(len(self.dev_data)):
            print(self.dev_data[index]["paragraphs"][0]["context"])
            print()
            for i in self.dev_data[index]["paragraphs"][0]["qas"]:
                print(i["question"])
                print(i["answers"][0]["text"], " ---- answer start", i["answers"][0]["answer_start"])
                print()
    def split_data(self,data="train"):
        self.splitted_data_root="dataset/splitted_data"
        if not os.path.exists(self.splitted_data_root):
            os.makedirs(os.path.join(self.splitted_data_root))
        contexts=open("{}/{}.context".format(self.splitted_data_root,data),"w")
        questions=open("{}/{}.question".format(self.splitted_data_root,data),"w")
        answers=open("{}/{}.answer".format(self.splitted_data_root,data),"w")
        current_data=None
        if(data=="train"):
            current_data=self.train_data
        else:
            current_data=self.dev_data
        
        for paragraph_id in range(len(current_data)):
            all_paragraphs=current_data[paragraph_id]["paragraphs"]
            for paragraph in all_paragraphs:
                context=paragraph["context"]

                all_qas=paragraph["qas"]
                for qa in all_qas:
                    curr_question=qa["question"]
                    all_answers=qa["answers"]
                    if(data=="train"):
                        #get the top answer
                        answer_id=1
                    
                    for i in range(answer_id):
                        answer=qa["answers"][i]["text"]
                    contexts.write(context+"\n")
                    questions.write(curr_question+"\n")
                    answers.write(answer+"\n")
        contexts.close()
        questions.close()
        answers.close()
                    



dataset=TQuadDataset()
dataset.split_data()