## Lesson: Optimization target shapes model behavior more than feature choice.
Initial model was hyperparameter-tuned with scoring='recall'. GridSearchCV picked class_weight={0:1, 1:5} to maximize recall, which systematically inflated predicted probabilities. ROC AUC was acceptable (0.63), but Brier score (0.2247) was worse than baseline (0.1598) and the calibration curve showed every bucket under the diagonal. Retuning with scoring='neg_brier_score' selected class_weight=None and lighter regularization, producing honestly-calibrated probabilities (Brier 0.1480, beats baseline). Lesson: pick the scoring metric based on how the model will be used, not by default.
## Lesson: Calibration curve right-tail noise vs. real mis-calibration.
After Brier-tuning, calibration curve looked clean on the left (predictions ≤ 0.5) but jagged and falling on the right (predictions > 0.5). Initial hypothesis was FICO under-training of high-risk loans. Diagnosed by counting sample size per probability bin: 0.70-1.00 range had only ~100 loans combined out of 269K. Conclusion: not a calibration failure — sample-size noise in an imbalanced dataset where the model honestly only puts ~0.1% of loans above 70% confidence. Lesson: always check bin sample sizes before reading calibration curve as truth.
## Lesson: Imbalanced data + calibrated model = recall on predict() drops.
Retuning for calibration dropped class-1 recall from 0.63 to 0.03. This is expected — honest probabilities for an 80/20 dataset rarely cross the default 0.5 threshold, so predict() flags almost nobody. For threshold-based hard classification, this would be a problem. For probability-based decision support (the Buy Here Pay Here  use case), it's fine — probability is the deliverable, not the binary label.
## Lesson: Brier Score vs ROC AUC a a metric for success.
Using Brier score is the smart play because the app returns the probability a customer will default not a hard default/no default binary return. This keeps the underwriter in the loop as the final decision rests with him, versus a model that makes the decision automatically. 

## Open Question: What all goes in the GridSearchCV?
max_iter and tol do not, they go outside seeing as max_iter is just giving it enough turns once it reaches it optimal goal it stops regardless of how many iterations. 

others are C, solver, penalty, and l1 ratio these go in the GridSearchCV

## Open Question: My GridSearchCV was limited.  How can I improve it, to further improve calibration?
GridSearchCV has other parameters like penalty, and fit_intercept. 
penalty is a bit complicated it has l1, l2 and elasticnet which is a mix of both. the purpose of penalty is that while it makes the model less accurate, it keeps it from memorizing the training data, and would be more flexible and understand new data.
l1 is a leash that deletes weak features while l2 shrinks all the features towards zero making the model quieter. elasticnet is a mix of both and requires l1_ratio to determine which combination to use. 
Some solver cannot use elasticnet or l1. 
Using them in GridSearchCV requires using a dictionary to match the solver to l2 and a different solver to what can use elasticnet.
fit_intercept is not applicable because all loans have an inherent probability of default and setting the baseline to 0 would screw with the calibration. 
with these knobs in the grid, the model can be fine tuned to increase calibration, and maybe roc auc. 

## Finding: ROC AUC slightly improved while tuning for Brier Score. 
The ROC AUC improved from 0.63 to 0.6867 when tuning for Brier Score with the recommendation from the GridSearchCV. 

## Finding: Brier Score does not budge past 0.1480 despite adjusting parameters after a rigorous GridSearchCV.
With C set at 0.1, penalty at l2, solver at newton-cg, and a class_weight of none the Brier Score remained at 0.1480 there was no improvement meaning that we have reached the ceiling of hyper parameter tuning. Other methods will be employed to improve the Brier Score.  The search included elasticnet, l1 as the other penalties, the class_weight from previous runs indicated none was the way to go. As for the solver, newton-cg with l2 penalty won.
In conclusion, we have reached the ceiling of hyperparameter tuning, to improve brier score other techniques such as FICO rebinning and CalibratedClassifierCV will be researched and employed. 







