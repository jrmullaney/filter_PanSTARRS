To make the filtered reference catalogue:

'''
python filterRefCatsAB.py
'''
which filters the original catalogue (in ps1_pv3_3pi_20170110/) to only include bright (Gmag<19) sources and converts fluxes and errors to AB mags. The filtered fits files are dumped into ps1_pv3_3pi_20170110_filteredAB.

'''
mkdir DATA
echo lsst.obs.test.TestMapper > DATA/_mapper
setup obs_test
''' 

'''
ingestReferenceCatalog.py DATA ./ps1_pv3_3pi_20170110_filteredAB/13*.fits --output refcat --configfile indexReferenceCatalogOverride.py &
ingestReferenceCatalog.py DATA ./ps1_pv3_3pi_20170110_filteredAB/14*.fits --output refcat --configfile indexReferenceCatalogOverride.py &
   ...
ingestReferenceCatalog.py DATA ./ps1_pv3_3pi_20170110_filteredAB/26*.fits --output refcat --configfile indexReferenceCatalogOverride.py &
'''
I found I needed to do this multiple times (i.e., as opposed to `*.fit`), as there were too many files to cope with in the ps1_pv3_3pi_20170110_filteredAB directory.

'''
mkdir ps1_pv3_3pi_20170110_GmagLT19
mv refcat/ref_cats/cal_ref_cat/* ./ps1_pv3_3pi_20170110_GmagLT19/
'''

Once you've tested that everything is ok, you can:
'''
rm -r ps1_pv3_3pi_20170110_filteredAB
'''
should you wish.
