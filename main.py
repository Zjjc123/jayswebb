import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

fits_image_filenames = ['JWST/jw02731-o001_t017_nircam_clear-f090w/jw02731-o001_t017_nircam_clear-f090w_i2d.fits',
                       'JWST/jw02731-o001_t017_nircam_clear-f187n/jw02731-o001_t017_nircam_clear-f187n_i2d.fits', 
                       'JWST/jw02731-o001_t017_nircam_clear-f200w/jw02731-o001_t017_nircam_clear-f200w_i2d.fits', 
                       'JWST/jw02731-o001_t017_nircam_clear-f335m/jw02731-o001_t017_nircam_clear-f335m_i2d.fits',
                       'JWST/jw02731-o001_t017_nircam_clear-f444w/jw02731-o001_t017_nircam_clear-f444w_i2d.fits',
                       'JWST/jw02731-o001_t017_nircam_f444w-f470n/jw02731-o001_t017_nircam_f444w-f470n_i2d.fits']

# make the filenames relative by adding a ./
fits_image_filenames = ['./' + filename for filename in fits_image_filenames]

# do the below but for all files in a loop
for filename in fits_image_filenames:
    hdul = fits.open(filename)
    dat = hdul[1].data

    # get the filename without the path
    name = filename.split('/')[-1].split('.')[0]
    print(name)
    
    plt.imsave("./export/" + name + ".png", np.log10(dat + abs(np.min(dat)) + 1), cmap='gray')
    # plt.imshow(np.log10(dat + 1), cmap='gray')
    # plt.show()
