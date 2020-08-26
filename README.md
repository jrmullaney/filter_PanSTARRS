To make the filtered reference catalogue:
1. Run:
   >> python filterRefCatsAB.py
   which filters the original catalogue (in ps1_pv3_3pi_20170110/) to only include bright (Gmag<19) sources and converts fluxes and errors to AB mags. The filtered fits files are dumped into ps1_pv3_3pi_20170110_filteredAB.
2. >> mkdir DATA
   >> echo lsst.obs.test.TestMapper > DATA/_mapper
3. >> setup obs_test 
4. >> ingestReferenceCatalog.py DATA ./ps1_pv3_3pi_20170110_filteredAB/13*.fits --output refcat --configfile indexReferenceCatalogOverride.py &
   >> ingestReferenceCatalog.py DATA ./ps1_pv3_3pi_20170110_filteredAB/14*.fits --output refcat --configfile indexReferenceCatalogOverride.py &
   ...
   >> ingestReferenceCatalog.py DATA ./ps1_pv3_3pi_20170110_filteredAB/26*.fits --output refcat --configfile indexReferenceCatalogOverride.py &
   You need to do this multiple times, as there are too many files to cope with in the ps1_pv3_3pi_20170110_filteredAB directory.
5. >> mkdir ps1_pv3_3pi_20170110_GmagLT19
   >> mv refcat/ref_cats/cal_ref_cat/* ./ps1_pv3_3pi_20170110_GmagLT19/
6. Once you've tested that everything is ok, you can:
   >> rm -r ps1_pv3_3pi_20170110_filteredAB
   should you wish.