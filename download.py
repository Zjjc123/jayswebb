from astroquery.mast import Observations

# 'NGC 3324': Carnia
# 'NGC 3132': Southern Ring Nebula
target_name = 'NGC 3324'

obs_table = Observations.query_criteria(target_name=target_name,obs_collection='JWST')

print(obs_table['obs_id'])

data_products = Observations.get_product_list(obs_table)

# Observations.filter_products(data_products,productType='SCIENCE',calib_level=[3],productSubGroupDescription='I2D')
preview_products = Observations.filter_products(data_products,productType='PREVIEW',calib_level=[3])

import os
os.mkdir(target_name)
Observations.download_products(preview_products,download_dir=target_name,flat=True)