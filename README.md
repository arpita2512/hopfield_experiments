# Hopfield Experiments   

This is an implementation of the Hopfield Network for COMP5400M Bio-Inspired Computing: Coursework 2. 
The task is to evaluate image reconstruction using synchronous pattern recovery, and compare results with the asynchronous 
approach and Self-Organising Map. Experiments are performed using the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. 

For implementation details and results, please see the [documentation](https://hopfield-experiments.readthedocs.io/).

### Directory Structure

```
├───hopfield_experiments
├   ├───docs
├   ├───hopfield_experiments
├       ├─── hopfield.py
├       └─── utils.py
├   ├─── Comparison_Digits.ipynb
├   ├─── Comparison_Plots.ipynb
├   ├─── Hopfield_Evaluation.ipynb
├   ├─── SOM_Evaluation.ipynb
├   ├─── README.md
├   ├─── mse_sync.pkl
├   ├─── mse_async.pkl
├   ├─── mse_som.pkl
├   ├─── psnr_sync.pkl
├   ├─── psnr_async.pkl
├   ├─── psnr_som.pkl
├   ├─── ssim_sync.pkl
├   ├─── ssim_async.pkl
├   ├─── ssim_som.pkl
└───└─── requirements.txt
```

### Description of Files

Comparison_Digits.ipynb
   --> Code for digit wise comparison of metrics

Comparison_Plots.ipynb
    --> Code for metric comparison aggregated across all digits

Hopfield_Evaluation.ipynb
    --> Code to generate a demo of reconstruction, a demo of spurious states, and evaluate metrics for synchronous hopfield network

SOM_Evaluation.ipynb
    --> Code to generate a demo of reconstruction and evaluate metrics for self organising map

### Reproduce Results

1. Unzip folder
2. Navigate to folder
```
cd hopfield_experiments
```
3. Install requirements
```
!pip install -r requirements.txt
```
4. Run desired ipynb file (see decriptions above)

### Statement of Contributions

The comparison with asynchronous approach was done using code from Ruchita Mijagiri.
