The unmodified datacards and workspaces from SNU are in Ingredients.

To modify the datacards and workspaces. This will place the new ones in Ingredients_Rebin:
```
python Rebin.py #Both scripts still need modifications to correct issues in datacards
python CorrectDataCards.py
```

To run limits locally:
```
combine -M AsymptoticLimits --run blind $CARDNAME
```

To run all limits on condor:
```
tar -zcvf CMSSW10213.tgz CMSSW_10_2_13 --exclude="CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/batch/2019_*" --exclude="CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/Ingredients/*" ###You must create a tarball of your working environment every time you update the datacards/workspaces.
./create-batch-Asymptotic -n <Jobname> -l cards_condor.txt ###You need to adjust create-batch-Asymptotic so that the paths of the Transfer_Input_Files are hardcoded to your location.
cd 2019_07_19_111603__Jobname
condor_submit submit.sh
```

When jobs have finished pipe the results into a txt file for plotting:
```
./read_Asymptotic.py -i 2019_07_19_111603__Jobname/ > 2019_07_19_111603__Jobname.txt
```



Put below rootfiles inside $CMSSE_BASE/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/MergedRootfiles/ :

EE_Boosted_SR_Bkgd.root
EE_Boosted_SR_Signal.root
EE_Resolved_SR_Bkgd.root
EE_Resolved_SR_Signal.root
MuMu_Boosted_SR_Bkgd.root
MuMu_Boosted_SR_Signal.root
MuMu_Resolved_SR_Bkgd.root
MuMu_Resolved_SR_Signal.root

Then, 

cd $CMSSE_BASE/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/MergedRootfiles 
python ExtractHistograms.py
python makecard.py

You will have datacards and shapes in $CMSSE_BASE/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/Ingredients/

