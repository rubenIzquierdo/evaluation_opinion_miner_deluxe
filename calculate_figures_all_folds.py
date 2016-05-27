#!/usr/bin/env python

import sys
import os
import glob

def read_data_entities(filename):
    fd = open(filename)
    lines = fd.readlines()
    fd.close()
    if len(lines)==0:
        return 0,0,0,0
    idx = 0
    while True:
        if lines[idx].startswith('%%%<DATA>%%%'):
            idx+=1
            break
        idx = idx+1
    fields_recall =  lines[idx].strip().split(' ')
    total_rec = int(fields_recall[0])
    ok_rec = int(fields_recall[1])
    fields_prec = lines[idx+1].strip().split(' ')
    total_prec = int(fields_prec[0])
    ok_prec = int(fields_prec[1])    
    return total_rec, ok_rec, total_prec,ok_prec


def read_data_relation(filename):
    fd = open(filename)
    lines = fd.readlines()
    fd.close()
    if len(lines) == 0:
        return 0,0,0
    idx = 0
    while True:
        if lines[idx].startswith('%%%<DATA>%%%'):
            idx+=1
            break
        idx = idx+1
    fields = lines[idx].strip().split(' ')
    ok = int(fields[0])
    wrong = int(fields[1])
    total = int(fields[2])
    return ok, wrong, total
    
if __name__ == '__main__':
    folder = sys.argv[1]
    folds = [f for f in glob.glob(folder+'/fold_*') if os.path.isdir(f)]
    print 
    print '#'*50
    print 'EVALUATION FOR:', folder,'with', len(folds),'folds'
    print 'Entity Evaluation:'
    L = ['expression','target','holder']
    for type_entity in L:
     
        total_rec = ok_rec = total_prec = ok_prec= 0
         
        for sub_folder in folds:
        #Expression
            trec, orec, tprec,oprec =  read_data_entities(sub_folder+'/evaluation.%s' % type_entity)
            total_rec += trec
            ok_rec += orec
            total_prec += tprec
            ok_prec += oprec
            
        if total_prec == 0:
            precision=0
        else:
            precision = ok_prec*100.0/(total_prec)
        
        if total_rec == 0:
            recall = 0
        else:
            recall = ok_rec*100.0/(total_rec)
        print '\t',type_entity
        print '\t\tPrecision: %.2f' % precision
        print '\t\tRecall:    %.2f' % recall
        if precision+recall == 0:
            F = 0
        else:
            F = 2*precision*recall/(precision+recall)
        print '\t\tF:    %.2f' % F
        
    print 'Relation Evaluation'
    for type_relation in ['expression_target', 'expression_holder']:
        total_ok = total_wrong = total_total = 0 
        for sub_folder in folds:
            tok, twr, tto = read_data_relation(sub_folder+'/evaluation.%s' % type_relation)
            total_ok += tok
            total_wrong += twr
            total_total += tto
        
        if (total_ok + total_wrong) == 0:
            precision = 0
        else:
            precision = total_ok * 100.0 / (total_ok + total_wrong)
        
        if total_total == 0:
            recall = 0
        else:
            recall = total_ok *100.0 / total_total
        print '\t',type_relation
        print '\t\tPrecision: %.2f' % precision
        print '\t\tRecall:    %.2f' % recall
        if precision+recall == 0:
            F = 0
        else:
            F = 2*precision*recall/(precision+recall)
        print '\t\tF:    %.2f' % F  
    print '#'*50
    print
        
        
        
         
    