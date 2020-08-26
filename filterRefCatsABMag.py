from astropy.io import fits
from astropy import units as u
from lsst.afw.image import abMagErrFromFluxErr, abMagFromFlux
import numpy as np
import glob
import os

files = glob.glob('ps1_pv3_3pi_20170110/*.fits')

for file in files:

    hdu = fits.open(file)
    
    hdu[1].columns.change_name('g_flux', 'g')
    hdu[1].columns.change_name('r_flux', 'r')
    hdu[1].columns.change_name('i_flux', 'i')
    hdu[1].columns.change_name('z_flux', 'z')
    hdu[1].columns.change_name('y_flux', 'y')
    
    hdu[1].columns.change_name('g_fluxSigma', 'g_err')
    hdu[1].columns.change_name('r_fluxSigma', 'r_err')
    hdu[1].columns.change_name('i_fluxSigma', 'i_err')
    hdu[1].columns.change_name('z_fluxSigma', 'z_err')
    hdu[1].columns.change_name('y_fluxSigma', 'y_err')

    hdu[1].columns.change_unit('coord_ra', 'deg')
    hdu[1].columns.change_unit('coord_dec', 'deg')
    
    areNans = np.isnan((hdu[1].data['g'],
                        hdu[1].data['r'],
                        hdu[1].data['i'],
                        hdu[1].data['z'],
                        hdu[1].data['y'],
                        hdu[1].data['g_err'],
                        hdu[1].data['r_err'],
                        hdu[1].data['i_err'],
                        hdu[1].data['z_err'],
                        hdu[1].data['y_err']))
    areNans = np.logical_or.reduce(areNans)
    hdu[1].data = hdu[1].data[~areNans]
    
    #Limit to brighter than 19th mag in g-band
    bright = hdu[1].data['g'] > 9.12e-5
    hdu[1].data = hdu[1].data[bright]
    
    hdu[1].data['g_err'] = abMagErrFromFluxErr(hdu[1].data['g_err'].astype(np.float),
                                                    hdu[1].data['g'].astype(np.float))
    hdu[1].data['r_err'] = abMagErrFromFluxErr(hdu[1].data['r_err'].astype(np.float),
                                                    hdu[1].data['r'].astype(np.float))
    hdu[1].data['i_err'] = abMagErrFromFluxErr(hdu[1].data['i_err'].astype(np.float),
                                                    hdu[1].data['i'].astype(np.float))
    hdu[1].data['z_err'] = abMagErrFromFluxErr(hdu[1].data['z_err'].astype(np.float),
                                                    hdu[1].data['z'].astype(np.float))
    hdu[1].data['y_err'] = abMagErrFromFluxErr(hdu[1].data['y_err'].astype(np.float),
                                                    hdu[1].data['y'].astype(np.float))
    
    hdu[1].data['g'] = abMagFromFlux(hdu[1].data['g'].astype(np.float))
    hdu[1].data['r'] = abMagFromFlux(hdu[1].data['r'].astype(np.float))
    hdu[1].data['i'] = abMagFromFlux(hdu[1].data['i'].astype(np.float))
    hdu[1].data['z'] = abMagFromFlux(hdu[1].data['z'].astype(np.float))
    hdu[1].data['y'] = abMagFromFlux(hdu[1].data['y'].astype(np.float))

    hdu[1].data['coord_ra'] = (180./np.pi)*hdu[1].data['coord_ra']
    hdu[1].data['coord_dec'] = (180./np.pi)*hdu[1].data['coord_dec']
    
    base = os.path.basename(file)
    newFile = 'ps1_pv3_3pi_20170110_filteredAB/'+base
    hdu.writeto(newFile, overwrite=True)
