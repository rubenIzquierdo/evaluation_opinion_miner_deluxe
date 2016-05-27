#!/usr/bin/env python

import sys

from collections import defaultdict

def load_data(filename):
    data = []
    fd = open(filename,'r')
    for line in fd:
        fields = line.strip().split('\t')
        if len(fields) == 3:
            label = fields[0]
            tokens = fields[1].split(' ')
            ids = fields[2].split(' ')
            data.append((label,tokens,ids))
    fd.close()
    return data


def evaluate(reference_data, comparison_data):
    total = ok = 0
    missed = defaultdict(int)
    for label, tokens, ids in reference_data:
        set_reference_ids = set(ids)
        total += 1
        correct = False
        for l_comp, tokens_comp, ids_comp in comparison_data:
            tokens_overlapping = set(ids_comp)  & set_reference_ids
            if len(tokens_overlapping) >= 1:
                ok += 1
                correct = True
                break
        if not correct:
            missed[' '.join(tokens)]+=1
            
    return missed, total, ok
        
    


if __name__ == '__main__':
    system_output_filename = sys.argv[1]
    system_data = load_data(system_output_filename)
    
    gold_filename = sys.argv[2]
    gold_data = load_data(gold_filename)
    
    ### PRECISION
    wrong_rec, total_prec, ok_prec = evaluate(system_data, gold_data)
    if total_prec == 0:
        precision=0
    else:
        precision = ok_prec*100.0/total_prec
    print '#'*50
            
            
    print 'Precision: %.2f Total system: %d' % (precision, total_prec)
    '''
    print 'Most wrong on the system:'
    for a, b in wrong_rec.items():
        if b > 1:
            print '\tFreq: %d --> %s' % (b,a)
    '''
    
    ### RECALL
    missed_rec, total_rec, ok_rec = evaluate(gold_data, system_data)
    if total_rec == 0:
        recall = 0
    else:
        recall = ok_rec*100.0/total_rec
    print 'Recall: %.2f Total gold: %d' % (recall, total_rec)
    '''
    print 'Most missed from the gold:'
    for a, b in missed_rec.items():
        if b > 1:
            print '\tFreq: %d --> %s' % (b,a)
    '''        
    print '#'*50    
    
    print '%%%<DATA>%%% (total_prec,ok_prec newline total_rec ok_rec'
    print total_prec, ok_prec
    print total_rec, ok_rec
    print '%%%</DATA>%%% (type, or, wrong)'        
            