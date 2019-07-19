HiggsAnalysis-CombinedLimit
===========================

### Official documentation

[Manual to run combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/)

### Standalone compilation on `cmslpc`

Need to use sl7 machines
```
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src/
cmsenv
git clone https://github.com/Michael-Krohn/HiggsAnalysis-CombinedLimit.git -b HNWR/v8.0.1 HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
scram b -j8
```

Our limit setting code is in HNWR_13TeV/ directory
