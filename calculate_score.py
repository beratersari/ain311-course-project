from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer

def BLUE_SCORE(output,references,n_gram=4):
    if(n_gram==4):
        weight=[0,0,0,1]
    if(n_gram==3):
        weight=[0,0,1,0]
    if(n_gram==2):
        weight=[0,1,0,0]
    if(n_gram==1):
        weight=[1,0,0,0]

    for qt_q in references:
        reference = [qt_q.split()]
        bleu_score=sentence_bleu(reference, output.split(),weights=weight)
        max_score=max(bleu_score,max_score)
    return max_score

def ROUGE_SCORE(output,references):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    for qt_q in references:
        scores = scorer.score(qt_q,output)
        scores['rouge1'].fmeasure
        scores['rougeL'].fmeasure
        max_score_1=max(scores['rouge1'].fmeasure,max_score_1)
        max_score_l=max(scores['rougeL'].fmeasure,max_score_l)     

    return max_score_1, max_score_l

def METEOR_SCORE(output,references):
    for qt_q in references:
        reference = [qt_q.split()]
        bleu_score=meteor_score(reference, output.split())
        max_score=max(bleu_score,max_score)
    return max_score