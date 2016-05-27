# EVALUATION OPINION MINER DELUXE#

In this repository we show the evaluation of the [opinion miner deluxe system](https://github.com/rubenIzquierdo/opinion_miner_deluxePP), for 6 languages (en, nl, de, es, it, fr) and 2 domains (hotel reviews and news).
All the intermediate evaluation output files are included for these criteria:

+ Six different languages: English, Dutch, German, Italian, Spanish and French
+ Two domains: hotel reviews and political news
+ Two experiments: (see paper)
+ Three opinion entities: opinion expression, opinion target and opinion holder
+ Two opinion entity relations: "is about" (relation between expression and target), and "is from" (relation between expression and holder)

The evaluation has been performed by running 5 Fold Cross Validation on the data, obtaining the indiviual figures per fold and micro-averaging over all the folds. This is the structure
of the evaluation data: under the `evaluation` folder there are two subfolders, one for each experiment, and within each of these experiments there are several subfolders with the
name `opener.DOMAIN.LANG.5`, where DOMAIN stands for either hotel or news, and LANG is the language code for the language. There is also one file `opener.DOMAIN.LANG.5.evaluation` with
the overall figures for the experiment. For instance we can see the figures for the evaluation of the system on hotel reviews for English (experiment number 0):
```shell
cat evaluation/exp0/opener.hotel.en.5.evaluation 
##################################################
EVALUATION FOR: opener.hotel.en.5 with 5 folds
Entity Evaluation:
	expression
		Precision: 87.76
		Recall:    77.49
		F:    82.31
	target
		Precision: 75.41
		Recall:    84.85
		F:    79.85
	holder
		Precision: 88.85
		Recall:    92.02
		F:    90.41
Relation Evaluation
	expression_target
		Precision: 70.53
		Recall:    74.23
		F:    72.34
	expression_holder
		Precision: 77.10
		Recall:    73.37
		F:    75.19
##################################################
```

To check the individual evaluation per fold, and the specific output of the system, you will need to access to the evaluation folds. For instance, the same experiment as before, evaluation
of the system on hotel reviews for English, if you check the `fold_0` you will find these files:
```
evaluation_opinion_miner_deluxe$ ls -1 evaluation/exp0/opener.hotel.en.5/fold_0

evaluation.expression               --> Evaluation of the opinion expression entity
evaluation.expression_holder        --> Evaluation of the IS FROM relation (expression-holder)
evaluation.expression_target        --> Evaluation of the IS ABOUT relation (expression-target)
evaluation.holder                   --> Evaluation of the opinion holder entity
evaluation.target                   --> Evaluation of the opinion target entity
expression.crfout                   --> Output of the CRF tagger for opinion expressions
expression_holder.gold              --> Gold data for IS FROM relation
expression_holder.output            --> System oufput for IS FROM relation
expression.sequences                --> Sequences extracted from the CRF output for expressions
expression_target.gold              --> Gold data for IS ABOUT relation
expression_target.output            --> System oufput for IS ABOUT relation
gold.expression                     --> Gold data for opinion expressions
gold.holder                         --> Gold data for opinion holders
gold.target                         --> Gold data for opinion targets
holder.crfout                       --> Output of the CRF tagger for opinion holders
holder.sequences                    --> Sequences extracted from the CRF output for holders
model.expression                    --> Trained model for opinion expressions
model.holder                        --> Trained model for opinion holders
model.target                        --> Trained model for opinion targets
parameters.expression               --> Parameters for opinion expression training
parameters.holder                   --> Parameters for opinion holder training
parameters.target                   --> Parameters for opinion target training
resources                           --> Folder with resources for this experiment
target.crfout                       --> Output of the CRF tagger for opinion targets
target.sequences                    --> Sequences extracted from the CRF output for targets
test                                --> List of files used for evaluation
train                               --> List of files used for training
```


