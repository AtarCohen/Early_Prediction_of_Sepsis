<h1> TODO </h1>
<ol>
<li> לסדר את הגיט ככה שישארו רק קבצים נחוצים ושהכל יהיה בתיקיות הנכונות כדי שהקבצים ירוצו בלי בעיה
</li>
<li> Upload processed CSV files from the machine to GIT </li>
<li> Upload Trained non-temporal models to GIT after training </li>
<li> Clone Git repo into azure machine </li>
<li> Delete current hw1_env and re install with the yaml file </li>
<li>  run both predict.py on the trained models, including reading psv files from the test directory as instructed
(The reading part is currently commented to save time). <br>
<b>  I assume parts 4-6 will take 1-2 hours (and maybe some more debuging since were cloning the repo)</b>
</li>
</ol>

<h2>Final Files - (לדעתי) </h2>
<ol>
<li>
Exploration
<ol> 
<li>
TemporalDataExploration.ipynb
</li>
<li>
NonTemporalExploration.ipynb - לוודא שמעודכן אחרי השינויים של עטר היום
</li>
</ol>
<li>
DataProcessing
<ol>
<li>
PrepareData.ipynb (currently in /notebooks)
</li>
<li>
DataPreparators.py</li>
</ol>
</li>
<li> Non Temporal Models
<ol>
<li>
Feature_Selection_Not_Serial.py (maybe change its name)
</li>
<li>
predict_ns.py (name need to change to predict.py assuming this will be our best model)
</li>
</ol>
</li>
<li> RNN Models
<ol>
<li> LSTM_Model.py </li>
<li> LSTM_main.py </li>
<li> trainer.py </li>
<li>predict_LSTM.py </li>
</ol>
</li>
<li> Explain_Models.ipynb</li>
<li> enivornment.yaml </li>
<li> readme? </li>
</ol>