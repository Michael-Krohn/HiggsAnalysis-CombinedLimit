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
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
source env_standalone.sh 
make -j 8; make # second make fixes compilation error of first
```
