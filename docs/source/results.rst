######################
Results
######################

Metrics Used
*******************
#. Mean squared error (MSE)
#. Peak signal-to-noise ratio (PSNR)
#. Structural similarity (SSIM)

Evaluation Strategy
**********************

Synchronous Hopfield Network
*****************************

.. image:: assets/sync_mse.png
  :width: 400

.. image:: assets/sync_psnr.png
  :width: 400

.. image:: assets/sync_ssim.png
  :width: 400

Self-Organising Map
**********************

.. image:: assets/som_mse.png
  :width: 400

.. image:: assets/som_psnr.png
  :width: 400

.. image:: assets/som_ssim.png
  :width: 400

Sync HN vs Async HN vs SOM
****************************

Metrics aggregated across all 10 digits.

*Note: Metrics for Asynchronous Hopfield Network are derived using Ruchita Mijagiri's code*

.. image:: assets/agg_mse.png
  :width: 400

.. image:: assets/agg_psnr.png
  :width: 400

.. image:: assets/agg_ssim.png
  :width: 400
