from nltk.translate.bleu_score import sentence_bleu
from transformers import MT5ForConditionalGeneration, AutoTokenizer
import calculate_score

tr=pd.read_csv(config.df_root+"/train.csv")
vl=pd.read_csv(config.df_root+"/valid.csv")

model = MT5ForConditionalGeneration.from_pretrained(config.output_dir)
tokenizer = AutoTokenizer.from_pretrained("google/mt5-base")

def greedy_decoding (inp_ids,attn_mask):
    greedy_output = model.generate(input_ids=inp_ids, attention_mask=attn_mask, max_length=256)
    Question =  tokenizer.decode(greedy_output[0], skip_special_tokens=True,clean_up_tokenization_spaces=True)
    return Question.strip().capitalize()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
context_q=dict()
i=0
j=0
while (i<len(vl)-2):
    curr_context=vl["context"][i]
    context_q["Turkish Context: "+curr_context]=[]
    for j in range(i,len(vl)):
        if(curr_context==vl["context"][j]):
            context_q["Turkish Context: "+curr_context].append(vl["question"][j])
        else:    
            i=j
            break

blue_score=0
rouge_L_score=0
rouge_1_score=0
meteor_scoree=0
counter=0
for article in context_q.keys():
    encoding = tokenizer.encode_plus(article, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)
    max_score=0
    output = greedy_decoding(input_ids,attention_masks)
    blue_score+=calculate_score.BLUE_SCORE(output,context_q[article])
    rouge1,rougeL=calculate_score.ROUGE_SCORE(output,context_q[article])
    rouge_L_score+=rougeL
    rouge_1_score+=rouge1
    meteor_scoree+=calculate_score.METEOR_SCORE(output,context_q[article])
        
    counter+=1
print("Blue-4 Score",blue_score/counter)
print("Rouge-L Score",rouge_L_score/counter)
print("Rouge-1 Score",rouge_1_score/counter)
print("Meteor Score",meteor_scoree/counter)
