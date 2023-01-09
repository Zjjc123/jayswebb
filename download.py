from astroquery.mast import Observations

obs_table = Observations.query_criteria(target_name='NGC 3324',obs_collection='JWST')
print(obs_table['obs_id'])

data_products = Observations.get_product_list(obs_table)

# Observations.filter_products(data_products,productType='SCIENCE',calib_level=[3],productSubGroupDescription='I2D')
preview_products = Observations.filter_products(data_products,productType='PREVIEW',calib_level=[3])

Observations.download_products(preview_products,download_dir='downloads',flat=True)